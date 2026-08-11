# 《폭풍의 눈》 전역 READER_KNOWLEDGE_MATRIX — 2026-08-11

## 목적

전체 작품의 미스터리·배신·관계 불확실성을 **독자가 모르는 것**과 **독자가 현재 장면을 이해하기 위해 알아야 하는 것**으로 분리한다.

기본 계약:

```text
WITHHOLD_INFORMATION_NOT_CONTEXT
```

금지:

- POV가 자연스럽게 아는 사실을 독자만 속이기 위해 부자연스럽게 감추기.
- 현재 목표·위험·관계·행동 결과까지 미스터리처럼 숨기기.
- POV가 모르는 진실을 작가 편의로 내면에 넣기.

정보 등급:

```text
A — immediate / safety / practical
    기본 공유.

B — uncertain hypothesis
    가설이라고 표시. 성격과 증거에 따라 공유.

C — personal / source / organizational sensitive
    실제 character-specific reason이 있을 때 제한 가능.
```

정보를 숨기면 `말하지 않는 이유`뿐 아니라 **행동 흔적·비용·관계 변화**가 있어야 한다.

---

# 1. Part1 — world-expansion information architecture

## K01 — 출항 / Yellow infiltration / ship disaster

```yaml
primary_pov: Ian / Alice / Juan by chapter
pov_knows:
  - ordinary voyage context
  - immediate anomaly / attack evidence as encountered
reader_knows:
  - Yellow-linked intrusion is active
  - each protagonist has incomplete access to the whole event
reader_needs_now:
  - where each person is
  - immediate survival goal
  - whether the current threat is physical / mental / organizational
hidden_truth:
  - full Yellow objective
  - William's deeper design
  - complete occult cosmology
withholding_reason:
  - protagonists genuinely do not know
post_event_information_change:
  - ordinary world is no longer a safe default
```

**Gate:** current action causality must remain readable even when attacker identity is incomplete.

---

## K02 — Milly reunion → betrayal → first disappearance

```yaml
primary_pov: Ian
pov_knows:
  - Milly is his real friend
  - her current behavior is increasingly suspicious
pov_suspects:
  - she is connected to Yellow / hiding something
reader_knows:
  - enough behavioral evidence to distrust without erasing friendship
reader_needs_now:
  - Ian has a personal reason to hesitate
  - Milly is both emotionally important and operationally dangerous
hidden_truth:
  - exact cult role / future survival
  - whether the disappearing body proves death
withholding_reason:
  - body evidence is genuinely absent
behavioral_trace:
  - Ian records uncertainty but emotionally reacts as if he killed a friend
post_event_information_change:
  - `Milly dead` is emotional belief, not objective fact
```

**Failure to avoid:** narration must not say objective death if evidence does not establish it.

---

## K03 — Hatem same-face reveal

```yaml
primary_pov: Ian
secondary_pov: Alice only if scene value differs
pov_knows:
  - masked Hatem is a dangerous outsider working with Yellow
  - Milly used this exact face
reader_knows:
  - face identity is literal visual information once mask breaks
reader_needs_now:
  - Hatem and Milly are separate people
  - Ian is projecting because of the face
hidden_truth:
  - why Milly used Hatem's face
  - Hatem's exact other god
  - exact contract details
withholding_reason:
  - not verified / not necessary for immediate action
behavioral_trace:
  - Ian initially uses Milly-shaped expectations
  - Hatem pushes back against projection
post_event_information_change:
  - same face becomes relationship problem, not only mystery clue
```

### Critical false-suspense rule
Once Ian **sees the unmasked face clearly**, prose may not keep calling it only `some familiar face` for chapters merely to preserve reveal.
The reveal happens when the POV sees it.
The mystery that remains is **why**, not **what he saw**.

---

## K04 — Milly alive + Hatem alive simultaneously

```yaml
primary_pov: Ian
pov_knows:
  - Milly is alive
  - Hatem is alive
  - they have the same face
reader_knows:
  - same as POV
reader_needs_now:
  - they are different people with different motives
hidden_truth:
  - face-copy origin if still unverified
withholding_reason:
  - no source-backed answer yet
post_event_information_change:
  - Ian can no longer reduce one person to the other
```

This event should **close identity confusion while keeping origin mystery open.**

---

## K05 — Hatem death → hallucination

```yaml
primary_pov: Ian
pov_knows:
  - Hatem physically died
  - he is now seeing/hearing Hatem again
pov_suspects:
  - hallucination / trauma response
reader_knows:
  - actual Hatem has no post-death agency
reader_needs_now:
  - hallucination cannot provide unknown facts
hidden_truth:
  - exact medical/occult contribution to symptom may remain uncertain
withholding_reason:
  - Ian cannot cleanly diagnose his own psyche
behavioral_trace:
  - he tests perception against external evidence
  - symptom disappears/gets ignored around others
post_event_information_change:
  - Hatem becomes internal pressure, not exposition source
```

**STRICT:** if hallucinated Hatem answers an unknown question, it must evade or expose Ian's ignorance, not reveal truth.

---

## K06 — William / Black King / obedience-bias reveal

```yaml
primary_pov: Juan
secondary_pov: Alice only where independently valuable
pov_knows:
  - Juan has real body reactions and real later choices
  - some Carter-priority conditioning may predate recent transformation
  - William shaped important conditions of Juan's life
reader_knows:
  - conditioning exists at least as priority bias / trained pathway
reader_needs_now:
  - conditioning is NOT a simple remote-control command
  - Juan's real affection and artificial bias can coexist
hidden_truth:
  - exact percentage/origin of every feeling
  - whether every relational condition was deliberately planned
withholding_reason:
  - impossible or unsupported to prove cleanly
post_event_information_change:
  - Juan's certainty about his own and later Alice's choices destabilizes
```

### Romance safety rule
Never turn uncertainty into authorial verdict:
- `Alice's love was fake` — forbidden unless user explicitly changes canon.
- `science proved both loves 100% pure` — also forbidden.

The structural payoff is **how they choose under uncertainty.**

---

## K07 — William–Alice final negotiation + Largo hidden setup

```yaml
primary_pov: Alice
secondary_pov:
  - short Ian sensory read if valuable
  - short Juan body-warning if valuable
pov_knows:
  Alice:
    - William is politically/mentally dangerous
    - Largo is the familiar competent secretary beside him
  Ian:
    - room feels unnaturally ordered/stable
  Juan:
    - his body keeps checking Largo position
reader_knows:
  - William is objectively dangerous
  - secretary is present
reader_needs_now:
  - ideological conflict remains Alice vs William
hidden_truth:
  - Largo's top-tier power
  - `[규율]`
withholding_reason:
  - no objective use/proof occurs
misdirection:
  - Ian/Juan unease can reasonably be attributed to William / situation
post_event_information_change:
  - hidden seed exists without stealing climax
```

**Gate:** do not have narration secretly state `the real danger was Largo`.
Later payoff must become `both were dangerous in different ways`.

---

# 2. Bridge — memory / agency / partial information

## K08 — Ch47 Elliott junior introduction

```yaml
primary_pov: Ian
pov_knows:
  - Elliott is his capable junior
  - ethically uncomfortable methods / questions exist
reader_knows:
  - ordinary senior-junior relationship before Part2 antagonist context
reader_needs_now:
  - Elliott matters personally to Ian
hidden_truth:
  - future cult role / loop control / Dabin relationship
withholding_reason:
  - Ian does not yet know the later event
post_event_information_change:
  - a human relationship seed exists before antagonist reveal
```

Do not villain-telegraph too hard.

---

## K09 — Ch51~52 memory water / Juan forgets Alice

```yaml
primary_pov: Juan
secondary_pov: Ian only for memory ethics
pov_knows_before:
  - Juan knows Alice relationship context
pov_knows_during:
  - context paths disappear; he may retain bodily/emotional traces without explanation
reader_knows:
  - Alice still exists and relationship history occurred
reader_needs_now:
  - memory loss changes access to context, not objective history
hidden_truth:
  - no hidden cosmic answer is required
withholding_reason:
  - Juan literally cannot access memory
post_event_information_change:
  - recovery happens through evidence/context/choice traces
```

### Gate
Do not write:
`He forgot everything, but true love alone remembered.`

Prefer:
`He can reconstruct that Alice repeatedly waited, asked, chose, and that he made choices around her.`

---

## K10 — Ch53~57 Choseikan / outer armor / Ruba

```yaml
primary_pov: Juan / Ian by chapter
pov_knows_initially:
  - giant threat and protected child appear connected
reader_knows_initially:
  - incomplete structure
reader_needs_now:
  - who is attacking whom
  - child is not simply the monster
hidden_truth:
  - exact outer-armor relation until reveal
reveal_trigger:
  - physical separation / Garon information / observed behavior
post_event_information_change:
  - protection mechanism itself becomes threat
  - characters change behavior: ask child / do not fill memory for Ruba
```

Good reveal because it changes action, not just lore.

---

## K11 — Ch59 Igares `그 답은 찾았나요?`

```yaml
primary_pov: Juan
pov_knows:
  - he has not isolated one pure origin for every impulse
  - body reaction does not erase every later choice
  - Alice is not his owner
reader_knows:
  - same
reader_needs_now:
  - this is a partial agency answer, not romance resolution
hidden_truth:
  - whether Juan will finally trust Alice's repeated choice
  - whether he can contact her directly
post_event_information_change:
  - Juan can reject owner/master frame, but still avoids final relationship step
```

---

# 3. Part2 — information-asymmetry and trust

## K12 — Dabin loop claim / early warnings

```yaml
primary_pov: Dabin
secondary_pov: Jumin for verification
pov_knows:
  Dabin:
    - impossible future/death signals are happening to her
  Jumin:
    - observable medical anomalies
reader_knows:
  - enough evidence that this is not simple delusion
reader_needs_now:
  - what changed physically / temporally
  - what is hypothesis vs fact
hidden_truth:
  - exact loop mechanism
  - Elliott's complete knowledge
withholding_reason:
  - protagonists genuinely do not know
post_event_information_change:
  - Dabin moves from target of explanation to recorder/decision-maker
```

---

## K13 — Ch92~93 hidden room / institutional history

```yaml
primary_pov: Jumin
pov_knows:
  - discovered records / objects / photos
reader_knows:
  - only what the physical evidence actually supports
reader_needs_now:
  - Elliott has real guardian/institution history
  - adult Pang/Hwang are connected to Dowon operations but not necessarily shared childhood
hidden_truth:
  - Hwang childhood origin unless verified
  - details of Pang childhood beyond Taewonpa origin
withholding_reason:
  - source not verified
post_event_information_change:
  - institutional responsibility attaches accurately to Elliott
```

**P0 correction:** remove current false shared-Wilmarth childhood conclusion.

---

## K14 — Ch95 Hwang escort / capture team

```yaml
primary_pov: Dabin
pov_knows:
  - Hwang says he is protecting her under Elliott's order
  - his route may also constrain her
reader_knows:
  - Hwang is not automatically trusted
reader_needs_now:
  - Dabin has alternatives and chooses route
hidden_truth:
  - full extent of Hwang strength
  - capture faction identity
withholding_reason:
  - Hwang has not yet needed full force
behavioral_trace:
  - adjusts from command to permission after Dabin pushes back
post_event_information_change:
  - relationship moves one step toward conditional cooperation
```

Competence proof later Ch105 can reveal strength without changing this info boundary.

---

## K15 — Ch102 three factions label Dabin

```yaml
primary_pov: Dabin
secondary_pov: Alice only for power-layout value
pov_knows:
  - three groups define her differently
reader_knows:
  - all three want different forms of control/access
reader_needs_now:
  - Dabin's own immediate desire
hidden_truth:
  - some faction motives remain incomplete
post_event_information_change:
  - Dabin states the missing question
  - Alice asks it
```

This is the ideal example of **information asymmetry without context deprivation**.

---

## K16 — Ch104~105 missing night / Pang sword

```yaml
primary_pov: Dabin
pov_knows_ch104:
  - memory stops before police transfer
  - body/object evidence proves later action
  - sword name = Pang Muak
reader_knows_ch104:
  - same evidence; no authoritative filler
reader_needs_now:
  - the gap is real
  - sword/blood are physical traces
hidden_truth:
  - exact encounter
  - whose blood is on sword
withholding_reason:
  - Dabin genuinely does not remember
reveal_trigger_ch105:
  - loop/memory flash opens missing-night encounter
post_reveal:
  - why Dabin has Pang's sword can be answered
  - whose blood is on it may remain open if later stabbing is still unidentified
```

This avoids fake suspense because **Dabin herself does not know.**

---

## K17 — Ch106~108 dead trio / ownership

```yaml
primary_pov:
  - Dabin for personal horror
  - Jumin for forensic limits
  - Alice for institutional ownership language
pov_knows:
  - the bodies look like them
  - estimated death sequence can be measured
reader_knows:
  - physical evidence is real even if causality is unknown
reader_needs_now:
  - which observations are verified
  - what institutions want to do with bodies
hidden_truth:
  - how this branch/time state produced persistent corpses
withholding_reason:
  - no character yet has mechanism
post_event_information_change:
  - death becomes evidence / property dispute / agency problem
```

Do not let bodies disappear later without recorded disposition.

---

## K18 — Ch113~114 duplicated seconds / videos

```yaml
primary_pov: Jumin
secondary_pov: Alice for evidence interpretation
pov_knows:
  - mutually exclusive recordings exist
  - external records can preserve overwritten states
reader_knows:
  - same
reader_needs_now:
  - practical rule: not all records reset equally
hidden_truth:
  - full cosmological mechanism
withholding_reason:
  - not required for operational use
post_event_information_change:
  - prior/current selves can cooperate through surviving evidence
```

This is a good `reader_needs_now < total truth` example.

---

## K19 — Ch118 hotel / `회수 실패 6` / future-or-other-loop photo

```yaml
primary_pov: Dabin
pov_knows:
  - photos and contracts exist
  - capture network has repeated attempts / preserved records
  - one photo appears to depict later/current-alternate state
reader_knows:
  - same
reader_needs_now:
  - the network has cross-loop evidence
hidden_truth:
  - photo's exact evidence class: future / other loop / branch
withholding_reason:
  - genuinely unresolved
post_event_information_change:
  - capture faction knows more than current protagonists
```

**DEBT:** by late Part2, clarify at least the practical evidence class even if metaphysics stay ambiguous.

---

## K20 — Ch126 Dabin consent / stop rules

```yaml
primary_pov: Dabin
pov_knows:
  - repeated procedures can happen while she is unconscious
reader_knows:
  - exact consent limits are now explicit
reader_needs_now:
  - what Jumin/Alice may do when Dabin cannot speak
hidden_truth:
  - whether next procedure succeeds
post_event_information_change:
  - future action has a pre-authorized boundary, not blank permission
```

This is Category A safety information and should be explicit.

---

## K21 — Ch128 Facility 17 choice + Alice regression

```yaml
primary_pov: Dabin
secondary_pov: Alice only if internal regression value is needed
pov_knows:
  - several evidence streams point to Facility 17
  - dream alone is not enough
reader_knows:
  - same practical evidence
reader_needs_now:
  - decision is not already made by Alice / dream / Elliott
hidden_truth:
  - exact future result
pressure:
  - time is limited
planned_conflict:
  - Alice pushes for quick decision
  - Dabin asserts that not-yet-choosing is also a choice
post_event_information_change:
  - Alice corrects behavior before final climax
```

This creates a genuine agency test rather than an explained principle.

---

## K22 — Ch129~130 Dabin / Elliott personal call

```yaml
primary_pov: Dabin
pov_knows:
  - Elliott remembers more loops
  - he has both saved and harmed her
  - his desired salvation = failed-future removal / fixed future
reader_knows:
  - enough to understand his ideology
reader_needs_now:
  - he genuinely wants Dabin alive
  - Dabin genuinely fears unknown future too
hidden_truth:
  - exact last-loop outcome
withholding_reason:
  - not required for moral decision
post_event_information_change:
  - Dabin refuses salvation while still acknowledging relationship
```

Do not turn him into a liar who never cared.

---

## K23 — Ch135 Juan cameo

```yaml
primary_pov: Dabin/Alice axis
juan_information:
  - can identify/stop external pressure or open route
reader_needs_now:
  - Juan is not here to solve Dabin's loop
hidden_truth:
  - Juan/Alice unresolved relationship remains elsewhere
post_event_information_change:
  - external battlefield pressure reduced; central choice unchanged
```

**Gate:** no omniscient Juan explanation of Elliott/time mechanics.

---

## K24 — Ch141+ procedure / stop choice

```yaml
primary_pov: Dabin / Jumin
pov_knows:
  - risks and prior failures recorded
  - Dabin stop condition is valid
reader_knows:
  - same safety-critical contract
reader_needs_now:
  - who owns stop decision
hidden_truth:
  - success result until procedure unfolds
post_event_information_change:
  - Alice/Jumin act within Dabin's declared boundary
```

---

## K25 — final Elliott confrontation

```yaml
primary_pov: Dabin
pov_knows:
  - Elliott loved/protected/used her
  - no perfect future safety exists without control
reader_knows:
  - all morally necessary facts for decision
reader_needs_now:
  - Dabin owns the final choice
hidden_truth:
  - future after choice
withholding_reason:
  - theme demands unknown future remain unknown
post_event_information_change:
  - Dabin kills Elliott
  - future becomes unknowable again
```

The unknown future is **payoff**, not missing exposition.

---

## K26 — Ch153 Ian/Elliott record

```yaml
primary_pov: Ian
pov_knows:
  - Elliott's old questions / his own mentorship history
  - institutional knowledge failures
reader_knows:
  - enough to see parallel with Ian's own knowledge ethic
hidden_truth:
  - no need for Elliott post-death secret message
post_event_information_change:
  - responsibility is recorded rather than buried
```

Sparse Hatem hallucination may comment only with Ian-known material.

---

## K27 — Ch155 Juan unsent message

```yaml
primary_pov: Juan
pov_knows:
  - Alice is alive / active
  - he can contact her
  - he wants to go
reader_knows:
  - Juan has real feelings
  - relationship remains unresolved
reader_needs_now:
  - this is avoidance, not lack of love
hidden_truth:
  - Alice's exact current answer
withholding_reason:
  - Juan refuses to ask
behavioral_trace:
  - opens number, composes possibilities, sends nothing
post_event_information_change:
  - practical obstacle is gone; emotional flaw remains
```

Later Rift scene should explicitly recontextualize this as partial self-protection disguised as respect.

---

# 4. Rift Accord — final reveal architecture

## K28 — Juan/Alice reunion

```yaml
primary_pov: Alice or Juan; choose one central POV per scene
reader_knows_before:
  - both care
  - Juan doubted origin and Alice's agency
  - no objective purity proof exists
reader_needs_now:
  - Alice's current choice and Juan's current choice must be spoken directly
hidden_truth:
  - none needed for romance payoff
post_event_information_change:
  - apology + present-choice confession
```

Do **not** hide Juan's known reason from his POV merely to delay confession again.

---

## K29 — Largo `[규율]` reveal

```yaml
primary_pov: preferably Ian or Juan observer for retroactive value
observer_knows_before:
  - Largo is unusually capable / instructor / secretary
  - old unexplained unease exists
reader_knows_before:
  - same
reader_needs_now:
  - someone disrupts summit
hidden_truth_until_trigger:
  - exact power name/scale
reveal_trigger:
  - power activation during meeting
payoff:
  - “회의 중입니다.”
  - `[규율]`
post_event_information_change:
  - Part1 order/body-warning is reinterpreted
```

Largo POV before reveal is less valuable if it would casually expose his own ability.

---

## K30 — Great Rift / managed tolerance

```yaml
primary_pov: summit participants / report readers
reader_knows_before:
  - classified mobilization hints
reader_needs_now:
  - ONE Great Rift exists
  - Pacific front is real
  - public explanation is wrong/incomplete
hidden_truth:
  - exact cosmic full truth may remain unknowable
reveal:
  - DG/military/corporations/awakened are holding the line
  - some managed tolerance of cult incidents is later policy
critical_boundary:
  - DG did NOT secretly create Part1/Part2 incidents
post_event_information_change:
  - survival compromise becomes next-era moral problem
```

---

# 5. Character-specific withholding rules

## Juan
May withhold:
- own pain / body condition.
- emotional uncertainty.

Must not withhold:
- immediate danger to protected people.

Narrative trace:
- minimizes own body in speech while POV notices movement/distance first.

---

## Alice
May withhold:
- source-sensitive DG information temporarily.
- personal hurt if current task demands composure.

Must not use `classified` as a lazy excuse to hide information Dabin needs for bodily consent.

Narrative trace:
- she notices faces/power/intent and sometimes chooses timing of disclosure.

---

## Ian
May withhold:
- uncertain hypothesis until enough evidence.
- sensitive source details.

Must clearly label:
- observation vs hypothesis vs unknown.

Hallucination cannot upgrade unknown → known.

---

## Jumin
Must default to Category A disclosure for:
- diagnosis risk.
- procedure options.
- stop conditions.

May delay interpretation until verification.

---

## Elliott
His defining flaw is **information paternalism**.

```text
knows more
→ predicts harm from full disclosure
→ tells only what he thinks others need
→ converts knowledge responsibility into decision authority
```

This should be shown as his actual behavior, not only explained in final debate.

---

## Largo
May withhold:
- classified DG operational detail.
- his own ability scale until relevant.

Must not withhold Juan information from Alice due jealousy.

His hidden affection does not justify information control.

---

# 6. Global information Gate

Before prose revision, each major reveal must answer:

```text
What does POV know?
What does reader know?
What does reader need now?
What is intentionally hidden?
Why is it hidden?
What behavioral trace does withholding leave?
What action becomes newly possible after reveal?
What old belief/scene is recontextualized?
```

High-risk failure codes:

- `CONTEXT_WITHHELD_AS_MYSTERY`
- `FALSE_SUSPENSE_BY_POV_SUPPRESSION`
- `AUTHOR_KNOWLEDGE_LEAK`
- `REVEAL_WITHOUT_RECONTEXTUALIZATION`
- `PAYOFF_WITHOUT_AFTERMATH`

With this matrix, the whole-work structural pass is ready for final P0/P1 consistency review before manuscript rewriting.
