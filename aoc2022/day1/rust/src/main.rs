use itertools::Itertools;
use std::cmp::Reverse;

fn main() -> color_eyre::Result<()> {
    color_eyre::install()?;
    // SOLUTION 1
    // let mut max = 0;
    // for group in include_str!("input.txt")
    //     .replace("\r\n", "\n")
    //     .split("\n\n")
    // {
    //     let mut sum = 0;
    //     for line in group.lines() {
    //         let value = line.parse::<u64>()?;
    //         sum += value;
    //     }
    //
    //     if sum > max {
    //         max = sum;
    //     }
    // }
    //
    // println!("The burdenesds eld is carrying {max} calories");

    // SOLUTION 2
    // let lines = include_str!("input.txt")
    //             .lines()
    //             .map(|v| v.parse::<u64>().ok())
    //             .collect::<Vec<_>>();
    // let groups = lines
    //     .split(|line| line.is_none())
    //     .map(|group| group.iter().map(|v| v.unwrap()).sum::<u64>())
    //     // .collect::<Vec<_>>();
    //     .max();
    // println!("groups = {groups:?}");

    // SOLUTION 3
    let ans = include_str!("input.txt")
        .lines()
        .map(|v| v.parse::<u64>().ok())
        .batching(|it| it.map_while(|x| x).sum1::<u64>())
        .map(Reverse)
        .k_smallest(3)
        .map(|x| x.0)
        .sum::<u64>();
    println!("{ans:?}");
    Ok(())
}
