# Extension notes

The paper identifies three central modeling choices: perfect substitutability,
linear effort cost, and myopic users. I checked each idea against the appendices
before treating it as open.

## Rejected as novel: convex effort cost

Replacing $c(e)=\gamma e$ with a strictly convex cost is the most immediate
idea, but Appendix D already develops it. It would be useful as replication,
not as a new extension.

## Candidate extension: a two-period, forward-looking agent

The static agent ignores how effort today affects skill tomorrow. A tractable
extension would add two periods:

1. Solve the second-period effort choice using Proposition 2.1.
2. Insert that optimized continuation value into the first-period problem.
3. Let first-period effort increase the probability of a higher second-period
   skill state.
4. Compare the resulting first-period effort with the myopic benchmark.

The equation that changes first is the period-one objective. Instead of current
utility alone, it includes a discounted continuation value:

$$
\max_{e_1\geq0}\;
p(s_1+e_1+a)-\gamma e_1
+\beta\,\mathbb{E}[V_2(s_2)\mid s_1,e_1].
$$

**Expected direction.** If effort raises the chance of future skill, a
forward-looking agent should exert weakly more effort than a myopic agent. The
interesting question is whether this response is strong enough to attenuate or
eliminate the deskilling paradox.

## Harder extension: nonadditive production

Adding complementarity between human inputs and AI changes the primitive
production function itself. This is economically interesting but harder to
scope because Sections 4.4 and 5.3 already interpret unreliability and AI
literacy as negative and positive interactions. A valid extension must be
distinguished carefully from those existing mechanisms.
