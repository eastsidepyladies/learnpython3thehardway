# Designing and Debugging

## Homework

### TO-DO
1. Planning
* Come up with concept
* Draw a map for game
* Create environment
* Populate environment
* Plan scenarios
2.  Create diagram and annotate with needed functions
3. Outline how source code should be organized using comments
4. Start writing code under comments, starting with what looks to be an easy section. Work towards runnable chunks so you can test as you go.
5. Run the whole dang thing to see if maybe it works.
6. Fix until it works.



## Notes

### RULES FOR IF STATEMENTS

* All if-statements must have an else
* if this else statement will never run bc it doesn't make sense, you must use a die function in the else that prints an error message and exits. Setting it up this way will be prove vury assistive.
* Never nest if-statements like paragraphs - put blank lines between so they are easier to read.
* Keep Boolean tests simple, stupid. If you want to complexify them, move calculations to variables early in the function and put some thought into their names.

### RULES FOR LOOPS

* Use while-loops only to loop forever, probs never. This applies to Python, other langs are diff.
* Use for-loops for other non-forever looping needs.

### TIPS FOR DEBUGGING

* Don't use debuggers, which are like full-body scans on sick people. TMI. Build in symptom trackers instead.
* Use print statements strategically to check values being assigned to variables
* Check code as you go so when you encounter a snarled rats nest, it's a more managable one.
