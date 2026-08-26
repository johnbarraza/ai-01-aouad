# Repository 1 — Aouad, Lykouris & Zhong (2026)

*Human-AI Productivity Paradoxes: Modeling the Interplay of Skill, Effort, and
AI Assistance* — [arXiv:2605.11350](https://arxiv.org/abs/2605.11350)

## Question and mechanism

Can AI reduce human effort while still raising output? The basic model isolates
one mechanism: skill, effort, and AI assistance are **perfect substitutes**.
They affect production only through total input

```math
x=s+e+a.
```

Thus, skill or AI can replace units of costly human effort one for one.

## The agent's problem

An agent with skill $s>0$ observes assistance $a\geq0$ and chooses effort
$e\geq0$:

```math
\max_{e\geq0}\;u(e,s,a)
=p(s+e+a)-\gamma e,
\qquad \gamma>0.
```

The production function $p:\mathbb{R}_{+}\to\mathbb{R}_{+}$ is weakly
increasing, weakly concave, continuous, and twice differentiable. The paper also
imposes

```math
\limsup_{x\to\infty}\frac{p(x)}{x}<\gamma,
```

which makes the relevant maximizing set nonempty and bounded.

## Proposition 2.1

Define the critical total input using the paper's largest-maximizer tie-break:

```math
x^*=\max\arg\max_{x\geq0}\{p(x)-\gamma x\}.
```

Then

```math
e^*(s,a)=(x^*-s-a)_+,
\qquad
p^*(s,a)=\max\{p(x^*),p(s+a)\},
```

where $(z)_+=\max\{z,0\}$.

**Intuition.** The worker targets $x^{\ast}$ units of total input. If skill plus AI
fall short, effort fills exactly the gap. If they already reach or exceed the
target, the nonnegativity constraint binds and effort is zero.

## Why the case split proves it

Set $x=s+e+a$. Because $e\geq0$, the transformed problem is

```math
\max_{x\geq s+a}\{p(x)-\gamma x\}+\gamma(s+a).
```

The final term is constant, so only the feasible lower bound matters.

- If $s+a\leq x^{\ast}$, the target remains feasible. Hence
  $x^{\mathrm{opt}}=x^{\ast}$ and $e^{\ast}=x^{\ast}-s-a$.
- If $s+a>x^{\ast}$, effort cannot reduce total input back to the target. Concavity
  makes net output fall to the right of the largest maximizer, so the best
  feasible point is $x^{\mathrm{opt}}=s+a$ and $e^{\ast}=0$.

Combining the cases yields the positive-part formula. Substituting the optimal
total input into $p$ yields the productivity formula.

## What I checked instead of trusting the AI

An initial AI answer tried to prove the proposition only from the first-order
condition $p'(s+e+a)=\gamma$. That argument is incomplete: it does not by itself
handle the corner $e=0$, a flat set of maximizers, or the paper's tie-break. I
therefore checked the change of variable and both feasible cases separately.
The raw exchange is in [`prompts.md`](prompts.md).

**Handwritten evidence:** add `hand/prop-2-1-case-split.jpg` before merge. It
must be the student's own photograph; [`hand/README.md`](hand/README.md) gives
the checklist.

## Repository contents

| Path | Purpose |
|---|---|
| `prompts.md` | Raw AI prompts and answers, followed by verification verdicts |
| `hand/` | Student's handwritten verification (photo still required) |
| `extensions.md` | Extensions considered and appendix check |
| `verify_proposition.py` | Numerical check for a smooth concave example |
| `presentation.tex` / `.pdf` | Five-minute Beamer deck |
| `paper/` | Citation and local download instructions |
