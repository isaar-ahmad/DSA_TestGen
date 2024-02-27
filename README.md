# DSA_TestGen
Testcase generator for DSA problem sets

Example :
Stage 1 : Testcase generation
1. Go to folder "standard-algorithms/sorting"
2. Run "sh script.sh"
3. Testcases will be generated in standard-algorithms/sorting/testcases/ folder.

---------------------------------------------------------------------------
Stage 2 : Testing 
1. Go to folder "regression"
2. Configure inputs in config.json :
	- Input #1 : Path to code-under-test
	- Input #2 : Path to reference testcases
	- Input #3 : Path to regression output (default : current folder)
----------------------------------------------------------------------------

TODO ( Stage 1 standard-algorithms/sorting )
1. Make config.json for testcase generation.
2. Remove spurious print statements.
3. etc.
