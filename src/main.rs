use std::collections::HashMap;

use clap::Parser;
use rand::Rng;

#[derive(Parser)]
struct Args {
    /// Number of times to run random function
    #[clap(short, long, default_value_t = 10)]
    sets: usize,

    /// Number of iterations per set
    #[clap(short, long, default_value_t = 1000)]
    reps: usize,

    /// Max degrees of freedom
    #[clap(short, long, default_value_t = 10)]
    df: usize,
}

fn main() {
    let args = Args::parse();
    run_random(args.sets, args.reps, args.df);
}

fn run_random(sets: usize, reps: usize, df: usize) {
    let mut rng = rand::thread_rng();
    let mut results: HashMap<usize, Vec<f64>> = HashMap::new();

    for _ in 0..sets {
        for n in 1..=df {
            let mut flips = Vec::new();
            for _ in 0..=reps {
                let num = rng.gen_range(0..=n);
                flips.push(num);
            }
            let expected_frequency = reps as f64 / (n as f64 + 1.0);
            let mut chis = Vec::new();
            for i in 0..=n {
                let observed_frequency = flips
                    .iter()
                    .filter(|res| res == &&i)
                    .collect::<Vec<_>>()
                    .len() as f64;
                let chi = chi(observed_frequency as f64, expected_frequency);
                chis.push(chi);
            }
            let entry = results.entry(n).or_default();
            entry.push(chis.iter().sum());
        }
    }
    println!("{:#?}", results);
}

fn chi(o: f64, e: f64) -> f64 {
    (o - e).powi(2) / e
}
