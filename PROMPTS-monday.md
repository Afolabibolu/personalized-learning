# Prompts for Monday

## 1. Set up the new files (paste once)

I have added these files to the repository: `CLAUDE.additions.md`, `docs/requirements.md`, `web/CLAUDE.md`, `ml/CLAUDE.md`, `supabase/CLAUDE.md`, `content/CLAUDE.md` and `content/sources/links.csv`.

Read all of them. Merge `CLAUDE.additions.md` into the root CLAUDE.md as it says, keeping everything already there, then delete it. Then compare `docs/requirements.md` with the actual code and tick any gap that is already done, with the file that proves it. Also update the existing resources to use the links in `links.csv` and reload them. Show me the updated gap list and stop.

## 2. Close the gaps (paste after step 1)

Read CLAUDE.md, `docs/requirements.md` and the CLAUDE.md in each folder you touch. Proceed with Phase 7. Start with FR5. After each requirement, stop and report: what changed, how to see it in the app, and which screenshots it enables. Wait for me to say "next" before the following requirement.

## 3. Results capture (after Phase 7)

Read CLAUDE.md and `docs/requirements.md`. Proceed with Phase 8. Run every test case for real and record the actual results, including any failures. Then give me the phase report and the screenshot list.

## 4. Course pipeline (stretch, only if Phase 8 is done)

Read CLAUDE.md and `content/CLAUDE.md`. Proceed with Phase 9 in the default mode, with no API key. Build `inventory.py` and show me its course table. After I pick one course from it, run `extract.py` for that course, write its files, validate, load, and stop.

## Running short on time

We are behind and the defence is tomorrow. Look at the open boxes in `docs/requirements.md`. Tell me which ones to drop so that FR4, FR5 and FR6 each have something visible to screenshot, and so Phase 8 still runs. List the cuts and wait for my yes.
