use num_bigint::BigInt;
use pyo3::prelude::*;

#[pymodule]
fn pyo3_bigint_overflow(_py: Python, m: &PyModule) -> PyResult<()> {
    #[pyfn(m, "to_string")]
    fn to_string(value: BigInt) -> String {
        format!("{}", value)
    }
    Ok(())
}
