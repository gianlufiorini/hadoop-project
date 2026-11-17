# Leonardo Da Vinci — Text analysis with MapReduce

ENSAI — Authors: [Gianluca Fiorini](https://github.com/gianlufiorini), [Aude Guerand](https://github.com/audeGrd)

We analyse [*The Notebooks of Leonardo Da Vinci*](https://www.gutenberg.org/ebooks/5000)
(Project Gutenberg #5000) with MapReduce jobs written in Python and run with
**Hadoop Streaming** (Hadoop 1.2.1). The project answers five questions:

1. frequency of words and of compositions of 2, 3, 4 and 5 words (n-grams);
2. number of words per word length (WordLengthCount);
3. top 2% most used letters in words longer than 4 and shorter than 10 letters;
4. the expected following word for a given word;
5. the sentences that include a given word.

## Requirements

- **Hadoop 1.2.1** installed in `~/simplehadoop`.
- This repository cloned in `~/Documents/hadoop-project`. These two paths are
  defined at the top of `run-tasks.sh` (variables `HADOOP` and `PROJECT`) and
  can be changed there.
- **Python 3.12 or newer**.
- The Python packages **`nltk`** (n-grams, tasks 1 and 4) and **`regex`**
  (preprocessing). They must be installed for the system `python3`, the one
  Hadoop calls, for example with `pip3 install nltk regex`: installing them
  only in a virtual environment is not enough.

The script `run-tasks.sh` runs the whole pipeline in one go (see
[What run-tasks.sh runs](#what-run-taskssh-runs)).

## Pipeline

```
data/ldv.txt ──0_preprocessing.py──► data/ldv_clean.txt
   (raw book)                         (one sentence per line)
                                             │
                          hadoop-data.sh: copy both files to HDFS (data/)
                                             │
                    task-1.sh … task-5.sh: MapReduce jobs on ldv_clean.txt
                                             │
                                  results in HDFS folders out-<name>
```

1. **Preprocessing** (local Python): the raw text is cleaned and rewritten with
   one sentence per line.
2. **Upload**: the raw and cleaned files are copied into HDFS.
3. **MapReduce jobs**: one job per question, all reading `ldv_clean.txt`; each
   job writes its result in an HDFS folder whose name is given as argument.

### Preprocessing choices

- The text is lowercased; tabs, line breaks and underscores (italics markers)
  are removed.
- Abbreviations (`fig.`, `no. 12`, `mss.`, `etc.`, units, months…) are
  protected so that their period does not end a sentence: the period is
  replaced by a `<DOT>` marker, which is kept in the cleaned text so that
  abbreviations remain distinguishable from ordinary words (e.g. `no<DOT>`
  for "No." versus the word "no").
- Contractions are expanded (`n't` → `not`, `'ve` → `have`, `'d` → `would`)
  and possessive `'s` is removed.
- A sentence ends with a period preceded by at least two letters or digits
  (so that web links are not broken), or with `?`, `!`; each sentence is
  written on its own line.
- All remaining punctuation is removed and spaces are normalised, so words are
  simply separated by single spaces.

## Repository structure

### Data — `data/`

| File | Content |
|---|---|
| `ldv.txt` | Raw book downloaded from Project Gutenberg. |
| `ldv_clean.txt` | Cleaned book: one sentence per line, lowercase words without punctuation. Input of all tasks. |

### Bash scripts — `scripts/bash/`

Arguments are positional, in the order given. All scripts except
`run-tasks.sh` use the `HADOOP` and `PROJECT` variables defined in
`run-tasks.sh`: to run one of them on its own, these two variables must be
defined first.

| Script | Arguments | Role |
|---|---|---|
| `run-tasks.sh` | — | Defines the `HADOOP` and `PROJECT` paths, then runs every step below in order. |
| `hadoop-start.sh` | — | (Re)starts the Hadoop daemons and checks them with `jps`. |
| `hadoop-data.sh` | file name without extension (`ldv`) | Runs the preprocessing on `data/<name>.txt`, then uploads the raw and cleaned files to the HDFS `data` folder (replacing old versions). |
| `task-1.sh` | n-gram size (1 to 5), output folder | Counts n-grams (1 = single words). |
| `task-2.sh` | output folder | Counts the number of words of each length. |
| `task-3.sh` | min length, max length (both excluded, `4` and `10`), fraction of letters (`0.02`), output folder | Finds the most used letters in the words between the two lengths. |
| `task-4.sh` | word, output folder | Lists the words that follow the given word. |
| `task-5.sh` | word, output folder | Lists the sentences containing the given word. |

The output folder is created in HDFS under the name `out-<output folder>`.

### Python scripts — `scripts/python/`

These scripts are called by the bash scripts, which pass their arguments.

| Script | Arguments | Role |
|---|---|---|
| `0_preprocessing.py` | file name without extension | Cleans `data/<name>.txt` as described above and writes `data/<name>_clean.txt`. |
| `map_1.py` | n-gram size | Emits `n-gram \t 1` for every sequence of n consecutive words of a sentence (n-grams never cross a sentence boundary). |
| `reduce_1.py` | — | Sums the counts of each n-gram; also used as combiner. |
| `map_2.py` | — | Emits `length \t 1` for every word. |
| `reduce_2.py` | — | Sums the counts of each key; used as reducer in task 2 and as combiner in tasks 2 to 5. |
| `map_3.py` | min length, max length | Emits `word \t 1` for every word whose length is strictly between the two bounds. |
| `reduce_3.py` | fraction of letters | Adds the count of each word to each of its letters, sorts the letters by frequency and keeps the top fraction of the 26 letters (rounded up). |
| `map_4.py` | word | Emits `next_word \t 1` for every bigram whose first word is the given word. |
| `reduce_4.py` | — | Sums the counts of each following word and sorts them by decreasing frequency. |
| `map_5.py` | word | Emits `sentence \t 1` each time the given word appears in a sentence. |
| `reduce_5.py` | — | Sums the counts per sentence and sorts the sentences by number of occurrences of the word. |

## What run-tasks.sh runs

`run-tasks.sh` starts Hadoop, cleans `data/ldv.txt` and uploads it to HDFS,
then runs the jobs below. Each result is written to the HDFS folder shown.

| Job | Arguments | Output folder |
|---|---|---|
| Task 1 — 2-grams | `2` | `out-1` |
| Task 1 — 3-grams | `3` | `out-2` |
| Task 1 — 4-grams | `4` | `out-3` |
| Task 1 — 5-grams | `5` | `out-4` |
| Task 2 — WordLengthCount | — | `out-5` |
| Task 3 — top letters | `4 10 0.02` (words of 5 to 9 letters, top 2%) | `out-6` |
| Task 4 — following word | `leonardo` | `out-7` |
| Task 5 — sentences | `leonardo` | `out-8` |

The example word `leonardo` can be replaced by any word in `run-tasks.sh`.
Single-word frequencies (task 1 with n = 1) are not run by default.

## Results and monitoring

- **Results** are stored in HDFS, in the `out-<output folder>` folders (files
  `part-*`). They can be browsed from the NameNode web interface,
  <http://localhost:50070>, with "Browse the filesystem".
- **Job execution** (progress of map and reduce tasks, duration, counters such
  as the number of records before and after the combiner, logs) can be followed
  on the JobTracker web interface, <http://localhost:50030>.

## Design notes

- Every job uses a combiner, which pre-aggregates counts on the map side and
  reduces the data sent through the shuffle.
- Jobs run with a single reducer, so that the outputs of tasks 3, 4 and 5 are
  globally sorted.
- In task 3, the map side only emits whole words and the reducer splits them
  into letters: the combiner can then aggregate identical words before the
  shuffle.
- Filtering on the given word is done in the mappers of tasks 4 and 5, so only
  relevant records reach the reducer.

## Limitations

- The Project Gutenberg header and licence are not removed, so their words are
  included in the counts.
- Numbers (section numbers, measures) are counted as words.
- Abbreviations keep their `<DOT>` marker: `no<DOT>` counts as a 7-character
  word in task 2, and in task 3 the letters D, O, T of the marker are counted
  (as uppercase letters).
- Task 3 only counts the 26 unaccented letters: accented letters of the Italian
  passages (è, à, ò…) are ignored.
- "Top 2%" is interpreted as 2% of the 26 letters, rounded up: task 3 returns a
  single letter.
- Sentences are only split after `.`, `?` or `!` followed by a space: in the
  tables of contents (`...(40--41).--The elements...`) several sentences stay
  on one line.
- Task 5 returns the cleaned sentence (lowercase, without punctuation), not the
  original text, and identical sentences are merged.
