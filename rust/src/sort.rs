fn swap(arr: &mut Vec<i32>, a: usize, b: usize) {
    let tmp = arr[a];
    arr[a] = arr[b];
    arr[b] = tmp;
}

fn merge(l: &Vec<i32>, r: &Vec<i32>) -> Vec<i32>{
    let mut merged =  vec![];

    let mut lndx = 0;
    let mut rndx = 0;
    while lndx < l.len() && rndx < r.len() {
        if l[lndx] < r[rndx] {
            merged.push(l[lndx]);
            lndx += 1;
        } else {
            merged.push(r[rndx]);
            rndx += 1;
        }
    }

    merged.extend(l[lndx..].to_vec());
    merged.extend(r[rndx..].to_vec());
    
    merged
}

pub fn bubble(arg: &Vec<i32>) -> Vec<i32> {
    let mut sorted = arg.clone();

    let mut end = arg.len();
    let mut is_sorted = false;
    while !is_sorted {
        is_sorted = true;
        for i in 1..end {
            let k = i-1;
            if sorted[k] > sorted[i] {
                swap(&mut sorted, i, k);
                is_sorted = false;
            }
        }
        end -= 1;
    }

    sorted
}

pub fn selection(arg: &Vec<i32>) -> Vec<i32> {
    let mut sorted = arg.clone();
    for i in 0..arg.len() {
        let mut smallest = i;
        for j in i..arg.len(){
            if sorted[j] < sorted[smallest] {
                smallest = j;
            }
        }
        swap(&mut sorted, i, smallest);
    }

    sorted
}

pub fn insertion(arg: &Vec<i32>) -> Vec<i32> {
    let mut sorted = arg.clone();

    for i in 1..sorted.len() {
        let mut back = i;

        while back > 0 {
            if sorted[back] < sorted[back - 1] {
                swap(&mut sorted, back, back - 1);
            } else {
                break;
            }
            back -= 1;
        }
    }

    sorted
}

pub fn merge_iter(arg: &Vec<i32>) -> Vec<i32> {
    let mut sorted = arg.clone();

    let mut section_size = 1;
    while section_size < sorted.len() {
        let iter = (0..sorted.len()).step_by(section_size * 2);
        for i in iter{
            let mut end = i + (section_size*2);
            if end >= sorted.len(){
                end = sorted.len();
            }

            let mut l = vec![];
            let mut r = vec![];

            for j in i..end {
                if j-i < section_size {
                    l.push(sorted[j]);
                } else {
                    r.push(sorted[j]);
                }
            }

            let merged = merge(&l, &r);

            for k in i..end {
                sorted[k] = merged[k-i];
            }
        }

        section_size *= 2
    }

    sorted
}

pub fn gravity(arg: &Vec<i32>) -> Vec<i32> {
    let mut sorted = vec![];

    let mut adj = 0; // adjustment value to ensure compatibility with negative numbers

    let mut lowest = arg[0];
    for i in 1..arg.len() {
        let x = arg[i];
        if x < lowest {
            lowest = x;
        }
    }
    
    if lowest <= 0 {
        adj = 1 - lowest;
    }

    let mut reversed = vec![];

    let mut beads = vec![];

    for x in arg.iter() {
        let k = x + adj;
        for i in 0..k as usize {
            if i >= beads.len() {
                beads.push(1);
            } else {
                beads[i] += 1;
            }
        }
    }


    while beads[0] > 0 {
        let mut n = 0;
        for i in 0..beads.len() {
            if beads[i] > 0 {
                n += 1;
                beads[i] = beads[i] - 1;
            } else {
                break;
            }
        }
        reversed.push(n);
    }

    reversed.iter().rev().for_each(|x| sorted.push(*x - adj));

    sorted
}