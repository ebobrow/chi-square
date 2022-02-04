# Chi Square

Running `cargo r --release -- --df 5 --sets 10000 --reps 100000` produced

![Program output](/img/10000x100000.png)

Running `cargo r --release -- --df 10 --sets 10000 --reps 100000` produced

![Program output](/img/10df.png)

More examples in /img folder

Bonus: chi square calculation in APL

```apl
chi ← +/((-×-)÷⊢)
```
