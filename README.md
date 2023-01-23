# id2id

## How to update and save id2id table in cloud storage (GitHub Releases and Zenodo)

1. Clone this repo.
2. Update the datasets in this repo (and commit it).
3. Create a Git tag (for this repo).
4. Push 2. and 3. here (== github.com/ecell/id2id).

Doing the above will automatically create an id2id table (TSV) with GitHub Actions and save it to GitHub Releases (https://github.com/ecell/id2id/releases) and Zenodo(https://zenodo.org/record/7562297).

## id2id table column definitions

| identifiersorgprefix1 | id1 | identifiersorgprefix2 | id2 |
|-----------------------|-----|-----------------------|-----|
| ...                   | ... | ...                   | ... |

## How to reproduce id2id table

Follow the workflow described in https://github.com/ecell/id2id/blob/main/.github/workflows/createid2id.yml
