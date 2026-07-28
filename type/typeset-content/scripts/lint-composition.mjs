#!/usr/bin/env node
/**
 * lint-composition.mjs — deterministic SAFE-AUTO composition scan.
 *
 * Reports (and optionally fixes) the character-level rules classified
 * SAFE-AUTO in references/COMPOSITION.md, while respecting exclusion zones.
 *
 * Usage, from the repository root:
 *   node skills/typeset-content/scripts/lint-composition.mjs "content/**\/*.md"
 *   node skills/typeset-content/scripts/lint-composition.mjs --fix "content/**\/*.md"
 *   node skills/typeset-content/scripts/lint-composition.mjs --json "src/**\/*.mdx"
 *
 * This handles the mechanical floor only. Anything CONTEXTUAL or NEVER-AUTO
 * is left to judgement — see the skill.
 */

import { readFileSync, writeFileSync } from "node:fs";
import { argv, exit } from "node:process";

const args = argv.slice(2);
const FIX = args.includes("--fix");
const JSON_OUT = args.includes("--json");
const globs = args.filter((a) => !a.startsWith("--"));

if (globs.length === 0) {
  console.error("usage: lint-composition.mjs [--fix] [--json] <files...>");
  exit(2);
}

/* ---------- exclusion zones ---------- */
/* Segments are protected by replacing them with placeholders before any
   text transform, then restored afterwards. Order matters: fenced code
   first, then inline code, then everything else. */

const ZONES = [
  { name: "fenced-code", re: /^```[\s\S]*?^```/gm },
  { name: "md-hr", re: /^[ \t]*(?:-{3,}|\*{3,}|_{3,})[ \t]*$/gm },
  { name: "md-table-delim", re: /^[ \t]*\|?[ \t]*:?-{2,}:?[ \t]*(?:\|[ \t]*:?-{2,}:?[ \t]*)*\|?[ \t]*$/gm },
  { name: "md-setext", re: /^[ \t]*={3,}[ \t]*$/gm },
  { name: "indented-code", re: /^(?: {4}|\t).*$/gm },
  { name: "html-code", re: /<(pre|code|kbd|samp|script|style)\b[\s\S]*?<\/\1>/gi },
  { name: "inline-code", re: /`[^`\n]*`/g },
  { name: "frontmatter", re: /^---\n[\s\S]*?\n---/ },
  { name: "url", re: /\b(?:https?:\/\/|www\.)[^\s<>"')\]]+/gi },
  { name: "email", re: /\b[\w.+-]+@[\w-]+\.[\w.-]+\b/g },
  { name: "path", re: /(?:^|\s)(?:\.{0,2}\/)[\w./-]+/g },
  { name: "html-attr", re: /<[a-z][^>]*>/gi },
  { name: "jsx-expr", re: /\{[^{}]*\}/g },
];

function protect(src) {
  const store = [];
  let out = src;
  for (const zone of ZONES) {
    out = out.replace(zone.re, (m) => {
      const token = `\u0000${store.length}\u0000`;
      store.push(m);
      return token;
    });
  }
  return { out, store };
}

function restore(src, store) {
  return src.replace(/\u0000(\d+)\u0000/g, (_, i) => store[Number(i)]);
}

/* ---------- SAFE-AUTO rules ---------- */

const ELISIONS =
  "(?:tis|twas|em|n|til|round|bout|cause|nother|kay|s|re|ve|ll|d|clock|" +
  "\\d{2}s)";

const RULES = [
  {
    id: "repeated-space",
    rule: "COMPOSITION.md#spaces-and-breaks",
    why: "Never two consecutive word spaces.",
    // Excludes runs abutting a pipe: that is Markdown table column padding,
    // which is alignment, not prose spacing.
    re: /([^\s|]) {2,}([^\s|])/g,
    fix: (m, a, b) => `${a} ${b}`,
  },
  {
    id: "sentence-double-space",
    rule: "COMPOSITION.md#spaces-and-breaks",
    why: "One space between sentences; two is a typewriter habit.",
    re: /([.!?]["')\u2019\u201d]?) {2,}(?=[A-Z\u201c\u2018])/g,
    fix: (m, a) => `${a} `,
  },
  {
    id: "ellipsis",
    rule: "COMPOSITION.md#marks-and-symbols",
    why: "An ellipsis is one character, not three periods.",
    re: /\.{3,}/g,
    fix: () => "\u2026",
  },
  {
    id: "em-dash",
    rule: "COMPOSITION.md#dashes-and-hyphens",
    why: "Never simulate a dash with multiple hyphens; en vs em is a judgement call.",
    automation: "CONTEXTUAL",
    re: /(\S)[ \t]*---[ \t]*(\S)/g,
    fix: (m, a, b) => `${a}\u2014${b}`,
  },
  {
    id: "en-dash",
    rule: "COMPOSITION.md#dashes-and-hyphens",
    why: "Never simulate a dash with multiple hyphens; en vs em is a judgement call.",
    automation: "CONTEXTUAL",
    re: /(\S)[ \t]*--[ \t]*(\S)/g,
    fix: (m, a, b) => `${a}\u2013${b}`,
  },
  {
    id: "elision-apostrophe",
    rule: "COMPOSITION.md#quotes-and-apostrophes",
    why: "Elisions take a closing apostrophe, not an opening quote. The classic '90s bug.",
    re: new RegExp(`(^|[\\s(\\[\u201c])['\u2018](${ELISIONS})\\b`, "gi"),
    fix: (m, pre, word) => `${pre}\u2019${word}`,
  },
  {
    id: "possessive-apostrophe",
    rule: "COMPOSITION.md#quotes-and-apostrophes",
    why: "Apostrophes point downward and take the closing form.",
    re: /(\w)'(\w)/g,
    fix: (m, a, b) => `${a}\u2019${b}`,
  },
  {
    id: "trailing-apostrophe",
    rule: "COMPOSITION.md#quotes-and-apostrophes",
    why: "Plural possessive takes a closing apostrophe.",
    re: /(s)'(?=\s|$|[.,;:!?])/g,
    fix: (m, a) => `${a}\u2019`,
  },
  {
    id: "double-quotes",
    rule: "COMPOSITION.md#quotes-and-apostrophes",
    why: "Use typographic quotes in prose.",
    re: /"([^"\n]+)"/g,
    fix: (m, inner) => `\u201c${inner}\u201d`,
  },
  {
    id: "copyright",
    rule: "COMPOSITION.md#marks-and-symbols",
    why: "Use the real symbol, not an alphabetic approximation.",
    re: /\((?:c|C)\)/g,
    fix: () => "\u00a9",
  },
  {
    id: "registered",
    rule: "COMPOSITION.md#marks-and-symbols",
    why: "Use the real symbol, not an alphabetic approximation.",
    re: /\((?:r|R)\)/g,
    fix: () => "\u00ae",
  },
  {
    id: "trademark",
    rule: "COMPOSITION.md#marks-and-symbols",
    why: "Use the real symbol, not an alphabetic approximation.",
    re: /\((?:tm|TM)\)/g,
    fix: () => "\u2122",
  },
];

/* ---------- scan ---------- */

function lineOf(src, index) {
  return src.slice(0, index).split("\n").length;
}

function scan(file) {
  const original = readFileSync(file, "utf8");
  const { out, store } = protect(original);
  let working = out;
  const findings = [];

  for (const rule of RULES) {
    rule.re.lastIndex = 0;
    let m;
    while ((m = rule.re.exec(working)) !== null) {
      findings.push({
        file,
        line: lineOf(working, m.index),
        id: rule.id,
        rule: rule.rule,
        severity: "Polish",
        automation: rule.automation ?? "SAFE-AUTO",
        observed: m[0].replace(/\n/g, "\\n"),
        recommended: rule.fix(...m).replace(/\n/g, "\\n"),
        why: rule.why,
      });
      if (rule.re.lastIndex === m.index) rule.re.lastIndex++;
    }
    if (FIX && (rule.automation ?? "SAFE-AUTO") === "SAFE-AUTO") {
      working = working.replace(rule.re, rule.fix);
    }
  }

  const fixed = restore(working, store);
  return { findings, changed: fixed !== original, fixed };
}

/* ---------- run ---------- */

let all = [];
let touched = 0;

for (const file of globs) {
  try {
    const { findings, changed, fixed } = scan(file);
    all = all.concat(findings);
    if (FIX && changed) {
      writeFileSync(file, fixed, "utf8");
      touched++;
    }
  } catch (err) {
    console.error(`skip ${file}: ${err.message}`);
  }
}

if (JSON_OUT) {
  console.log(JSON.stringify(all, null, 2));
} else if (all.length === 0) {
  console.log("No SAFE-AUTO composition findings.");
} else {
  console.log("| Severity | Auto | Location | Observed | Recommended | Why |");
  console.log("| --- | --- | --- | --- | --- | --- |");
  for (const f of all) {
    console.log(
      `| ${f.severity} | ${f.automation} | ${f.file}:${f.line} | \`${f.observed}\` | \`${f.recommended}\` | ${f.why} |`
    );
  }
  console.log(`\n${all.length} finding(s).${FIX ? ` ${touched} file(s) written.` : " Re-run with --fix to apply."}`);
}

const pending = all.filter((f) => f.automation !== "SAFE-AUTO").length;
if (FIX && pending) {
  console.log(`${pending} CONTEXTUAL finding(s) left for review — not auto-applied.`);
}
exit(all.length && !FIX ? 1 : 0);
