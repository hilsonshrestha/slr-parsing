# SLR Parsing
Step wise implementation of SLR parsing

- Generates Goto
- Calculates First and Follow
- Shifting and Reduction
- Generates parsing table
- String evaluation using parsing table.

# Running
```bash
python slr.py "grammar file location" "string to check"
```

Example:
```bash
python slr.py ./test_grammar/grammar1.txt "id + ( id * id )"
```

TODO: Removing left recursion
