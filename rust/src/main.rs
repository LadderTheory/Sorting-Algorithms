use rand::Rng;
use std::time::Instant;

mod sort;

struct SortAlg {
	name: Box<String>,
	alg: Box<dyn Fn(Vec<i32>) -> Vec<i32>>,
}

impl SortAlg {
	fn new(
		name: &str, 
		alg: Box<dyn Fn(Vec<i32>) -> Vec<i32>>,
	) -> SortAlg {
		SortAlg {
			name: Box::new(String::from(name)),
			alg: alg,
		}
	}
}

fn main() {
	let mut rng = rand::thread_rng();

	let mut unsorted = vec![0;25];
	let print = unsorted.len() <= 50;

	unsorted.iter_mut().for_each(|x| *x = rng.gen_range(-99,100));

	let bubble		= SortAlg::new("Bubble",Box::new(|x| sort::bubble(&x)));
	let selection	= SortAlg::new("Selection", Box::new(|x| sort::selection(&x)));
	let insertion	= SortAlg::new("Insertion",Box::new(|x| sort::insertion(&x)));
	let merge		= SortAlg::new("Merge", Box::new(|x| sort::merge_iter(&x)));
	let gravity		= SortAlg::new("Gravity", Box::new(|x| sort::gravity(&x)));

	let sorts = [
		bubble,
		selection,
		insertion,
		merge,
		gravity,
	];

	if print {
		println!("{:?}", &unsorted);
	}

	for s in sorts.iter() {
		let now = Instant::now();
		let sorted = (*s.alg)(unsorted.clone());
		let elapsed = now.elapsed().as_millis();
		println!("{} Time: {}", *s.name, elapsed);        
		if print {
			println!("{:?}", sorted);
		}
	}
}