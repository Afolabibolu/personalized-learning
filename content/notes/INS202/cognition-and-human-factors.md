# Cognition and Human Factors

## Perception

Users interpret interfaces through **visual, auditory and haptic** perception. The **Gestalt principles** describe how we group what we see: **proximity** (items close together seem related), **similarity**, **closure** and **continuity**. A common mistake is placing related controls far apart.

## Memory

Memory works in stages: **sensory**, **short-term (working)** and **long-term**. **Recall** means retrieving information from memory unaided; **recognition** means identifying it when shown, as in choosing from a visible menu. **Recognition is cognitively easier**, which is why menus are easier for novices than command lines. Amazon keeps the cart icon and item count visible so users need not recall their choices.

## Attention and learning

**Selective attention** focuses on one thing while filtering others; **divided attention** splits focus across several, with real limits on multitasking. Notifications should have a clear hierarchy, and non-essential alerts should be silenced during safety-critical tasks. Users progress from **novice to expert**, so good design supports both first-time success and expert speed (**learnability**).

## Mental models

**Norman** distinguishes the **designer's model** (how the designer thinks the system works), the **system image** (what the interface actually communicates) and the **user's model** (how the user believes it works). Designers should not assume users understand the system as they do, and should test and revise the system image.

## Slips and mistakes

**Reason's taxonomy**:

- A **slip** has a **correct intention but incorrect execution**, caused by inattention, habit or poor physical design. Pressing the wrong digit of a known PIN on a cramped keypad is a slip; Gmail's **"Undo Send"** fixes a common slip.
- A **mistake** has an **incorrect intention**, carried out as planned, from flawed understanding.

**Errors are design signals**, not careless users to blame.

## The laws

- **Cognitive load** is the total mental effort in working memory; cluttered dashboards increase it.
- **Miller's Law (1956)**: people hold about **seven, plus or minus two** (five to nine) items in short-term memory, so **group menu items into chunks of 5 to 9**.
- **Fitts's Law** predicts the time to select a target: **T = a + b × log₂(2D / W)**, where D is the distance and W the target width. With a = 50 ms and b = 150 ms, a 100px button 200px away takes 50 + 150 × log₂(4) = **350 ms**, while a 20px button takes about **698 ms**. So **make critical buttons large and close**.
- **Hick's Law** predicts decision time: **T = b × log₂(n + 1)** for n choices. With b = 200 ms, 4 choices take about **464 ms** and 16 choices about **818 ms**. So **reduce simultaneous choices** and use hierarchical menus, as Google's single search box does.

Source: INS 202 Lecture 3 Cognition and Human Factors
