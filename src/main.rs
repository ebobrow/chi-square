use std::{collections::HashMap, fs};

use clap::Parser;
use pyo3::{prelude::*, types::IntoPyDict};
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

fn main() -> PyResult<()> {
    let args = Args::parse();
    let results = run_random(args.sets, args.reps, args.df);

    Python::with_gil(|py| {
        let module = PyModule::from_code(py, &fs::read_to_string("main.py").unwrap(), "", "")?;
        let func: Py<PyAny> = module.getattr("main")?.into();
        func.call1(py, (results.into_py_dict(py),))?;

        Ok(())
    })
}

fn run_random(sets: usize, reps: usize, df: usize) -> HashMap<usize, Vec<f64>> {
    let mut rng = rand::thread_rng();
    let mut results: HashMap<usize, Vec<f64>> = HashMap::new();

    for n in 1..=df {
        let expected_frequency = reps as f64 / (n as f64 + 1.0);
        for _ in 0..=sets {
            let mut flips = Vec::with_capacity(reps);
            for _ in 0..=reps {
                flips.push(rng.gen_range(0..=n));
            }
            let mut chis = Vec::with_capacity(n);
            for i in 0..=n {
                let observed_frequency = flips.iter().filter(|res| res == &&i).count() as f64;
                chis.push(chi(observed_frequency, expected_frequency));
            }
            let entry = results.entry(n).or_insert(Vec::with_capacity(sets));
            entry.push(chis.iter().sum());
        }
    }
    results
}

fn chi(o: f64, e: f64) -> f64 {
    (o - e).powi(2) / e
}
