# Chi Square

Running `cargo r --release -- -d 5 -s 10000 -r 100000` produced

![Program output](/img/10000x100000.png)

Running `cargo r --release -- -d 10 -s 10000 -r 100000` produced

![Program output](/img/10df.png)

More examples in /img folder

Bonus: chi square calculation in APL

```apl
chi ← +/((-×-)÷⊢)
```
