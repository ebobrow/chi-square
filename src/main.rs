use std::env;

use rand::Rng;

fn main() {
    let mut args = env::args();
    args.next();
    let iters = args.next().map(|n| n.parse().ok()).flatten().unwrap_or(100);
    run_random(iters);
}

fn run_random(iters: i32) {
    let mut rng = rand::thread_rng();

    for n in 1..10 {
        let mut results = Vec::new();
        for _ in 0..=iters {
            let num = rng.gen_range(0..=n);
            results.push(num);
        }
        let expected_frequency = iters as f64 / (n as f64 + 1.0);
        let mut chis = Vec::new();
        for i in 0..=n {
            let observed_frequency = results
                .iter()
                .filter(|res| res == &&i)
                .collect::<Vec<_>>()
                .len() as f64;
            let chi = chi(observed_frequency as f64, expected_frequency);
            chis.push(chi);
        }
        println!("{}: {}", n, chis.iter().sum::<f64>());
    }
}

fn chi(o: f64, e: f64) -> f64 {
    (o - e).powi(2) / e
}
