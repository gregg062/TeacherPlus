# Week 3: Elimination (4 days: Monday is MLK Day)

Algebra 1 · Unit: Systems of linear equations and inequalities · Long-term sub package (EXAMPLE)

*Every answer in this file was computer-checked with `tools/check_math.py` (298/298 correct).*

## Day 11: Tuesday, January 19: Elimination by adding

**Learning target:** I can solve a system by adding the equations to eliminate a variable.  
**Standards:** HSA-REI.C.5, HSA-REI.C.6 (full text in the calendar)  
**Materials:** Do Now slide or board, guided notes handout, practice handout, exit ticket slips

### Run of show (50 minutes)

| Time | Segment | Notes |
|---|---|---|
| 0:00-0:07 | Do Now (silent, independent) | Problems on the board; answers in the key. Go over 1-2 quickly. |
| 0:07-0:20 | Mini-lesson: worked examples + find the mistake | Script below. Students copy the examples into their notes. |
| 0:20-0:30 | Guided practice (we do) | Do problem 1 together; students do 2-3 with a partner, then check on whiteboards or by showing work. |
| 0:30-0:45 | Independent practice (you do) | Circulate. See students on the support list first. Early finishers: challenge or next problems. |
| 0:45-0:50 | Exit ticket | Silent. Collect at the door and sort into got it / nearly / not yet. |

### Opening (say this)

"Substitution is great when a variable is easy to isolate. When the equations look like 3x + 2y = 12 and 5x − 2y = 4, there's a faster way. If we ADD the two equations, +2y and −2y cancel. We're allowed to add equations because we're adding equal things to both sides."

### Do Now

1. Solve by substitution:  x + y = 7  and  3x − y = 1.
2. Solve by substitution:  y = 3x + 1  and  6x − 2y = −2.
3. Identify the slope and y-intercept of y = −x + 4.

### Mini-lesson: worked examples (script)

**Worked example 1:** Solve by elimination:  3x + 2y = 12  and  5x − 2y = 4.

Write each step on the board and say what you're doing and why. Ask the question in italics before writing the step and give 3-5 seconds of think time.

1. Line up the equations in standard form:  (1) 3x + 2y = 12   (2) 5x − 2y = 4
2. Add the equations. The y terms cancel: 8x = 16
3. Divide both sides by 8: x = 2
4. Substitute x = 2 into equation (1): 3(2) + 2y = 12 → 2y = 6 → y = 3
5. Solution (2, 3). Check in equation (2): 5(2) − 2(3) = 4 ✓

Say: *"So the answer is (2, 3). How do we know it's right?"* (We checked it in the original equations.)

**Worked example 2:** Solve by elimination:  x + 4y = 7  and  −x + 3y = 7.

Write each step on the board and say what you're doing and why. Ask the question in italics before writing the step and give 3-5 seconds of think time.

1. Line up the equations in standard form:  (1) x + 4y = 7   (2) −x + 3y = 7
2. Add the equations. The x terms cancel: 7y = 14
3. Divide both sides by 7: y = 2
4. Substitute y = 2 into equation (1): x + 4(2) = 7 → x = −1
5. Solution (−1, 2). Check in equation (2): −(−1) + 3(2) = 7 ✓

Say: *"So the answer is (−1, 2). How do we know it's right?"* (We checked it in the original equations.)

**Find the mistake** (project or write this; ask students to find and explain the error with a partner for 2 minutes):

> Solve: 2x + 3y = 13 and 4x − 3y = −1.  
> Add: 6x = 14  
> x = 7/3  

*What's wrong:* The student added the left sides but forgot to add the right sides correctly: 13 + (−1) = 12, not 14.  
*Correct:* 6x = 12, x = 2, then 2(2) + 3y = 13 → y = 3. Solution (2, 3).

### Watch for (common mistakes and what to say)

- **Adding the left sides but not the right sides correctly.** Say: "Add straight down: x's, y's, AND the numbers."
- **Adding when the terms have the same sign (they don't cancel).** Say: "Opposites cancel. 2y + 2y is 4y, not 0. Next lesson we'll fix that by multiplying."

### Guided practice

1. Solve by elimination:  x + y = 5  and  x − y = 3.
2. Solve by elimination:  2x + 5y = 1  and  −2x + 3y = −9.
3. Solve by elimination:  4x − 3y = −6  and  x + 3y = 6.

### Independent practice

1. Solve by elimination:  3x + y = 10  and  2x − y = 0.
2. Solve by elimination:  −5x + 2y = 1  and  5x + 4y = 17.
3. Solve by elimination:  x − 6y = −3  and  2x + 6y = 12.
4. Solve by elimination:  7x + 3y = 5  and  −7x + 2y = 15.
5. Solve by elimination:  2x − 5y = 0  and  3x + 5y = 25.
6. Solve by elimination:  −4x + y = 5  and  4x + 3y = −17.

### Exit ticket

1. Solve by elimination:  5x + 2y = 9  and  3x − 2y = −1.
2. Solve by elimination:  −3x + 4y = 2  and  3x + y = 8.

**Sorting:** all correct = *got it* (start tomorrow's Do Now normally); one error = *nearly* (hand back with a hint tomorrow); both wrong or blank = *not yet* (sit with these students during tomorrow's guided practice). Record counts in the handoff log.

### Answer key (fully worked)

**Do Now 1.** Solve by substitution:  x + y = 7  and  3x − y = 1.  
**Answer: (2, 5)**
   - Solve the first equation for y: x + y = 7  →  y = −x + 7
   - Substitute (−x + 7) for y in the second equation, keeping the parentheses: 3x − (−x + 7) = 1
   - Distribute: 3x + x − 7 = 1
   - Combine like terms: 4x − 7 = 1
   - Add 7 to both sides: 4x = 8
   - Divide both sides by 4: x = 2
   - Substitute x = 2 into y = −x + 7: y = −(2) + 7 = 5
   - Solution (2, 5). Check in the second equation: 3(2) − (5) = 1 ✓

**Do Now 2.** Solve by substitution:  y = 3x + 1  and  6x − 2y = −2.  
**Answer: infinitely many solutions**
   - The first equation already says y = 3x + 1.
   - Substitute (3x + 1) for y in the second equation, keeping the parentheses: 6x − 2(3x + 1) = −2
   - Distribute: 6x − 6x − 2 = −2
   - Combine like terms: the x terms cancel, leaving −2 = −2
   - −2 = −2 is always true, so every point on the line works: infinitely many solutions (the equations are the same line).

**Do Now 3.** Identify the slope and y-intercept of y = −x + 4.  
**Answer: slope −1, y-intercept 4 (the point (0, 4))**
   - The equation is in the form y = mx + b, so the slope m is the number multiplying x and b is the constant.
   - m = −1, b = 4, so the line crosses the y-axis at (0, 4).

**Example 1.** Solve by elimination:  3x + 2y = 12  and  5x − 2y = 4.  
**Answer: (2, 3)**
   - Line up the equations in standard form:  (1) 3x + 2y = 12   (2) 5x − 2y = 4
   - Add the equations. The y terms cancel: 8x = 16
   - Divide both sides by 8: x = 2
   - Substitute x = 2 into equation (1): 3(2) + 2y = 12 → 2y = 6 → y = 3
   - Solution (2, 3). Check in equation (2): 5(2) − 2(3) = 4 ✓

**Example 2.** Solve by elimination:  x + 4y = 7  and  −x + 3y = 7.  
**Answer: (−1, 2)**
   - Line up the equations in standard form:  (1) x + 4y = 7   (2) −x + 3y = 7
   - Add the equations. The x terms cancel: 7y = 14
   - Divide both sides by 7: y = 2
   - Substitute y = 2 into equation (1): x + 4(2) = 7 → x = −1
   - Solution (−1, 2). Check in equation (2): −(−1) + 3(2) = 7 ✓

**Guided 1.** Solve by elimination:  x + y = 5  and  x − y = 3.  
**Answer: (4, 1)**
   - Line up the equations in standard form:  (1) x + y = 5   (2) x − y = 3
   - Add the equations. The y terms cancel: 2x = 8
   - Divide both sides by 2: x = 4
   - Substitute x = 4 into equation (1): (4) + y = 5 → y = 1
   - Solution (4, 1). Check in equation (2): (4) − (1) = 3 ✓

**Guided 2.** Solve by elimination:  2x + 5y = 1  and  −2x + 3y = −9.  
**Answer: (3, −1)**
   - Line up the equations in standard form:  (1) 2x + 5y = 1   (2) −2x + 3y = −9
   - Add the equations. The x terms cancel: 8y = −8
   - Divide both sides by 8: y = −1
   - Substitute y = −1 into equation (1): 2x + 5(−1) = 1 → 2x = 6 → x = 3
   - Solution (3, −1). Check in equation (2): −2(3) + 3(−1) = −9 ✓

**Guided 3.** Solve by elimination:  4x − 3y = −6  and  x + 3y = 6.  
**Answer: (0, 2)**
   - Line up the equations in standard form:  (1) 4x − 3y = −6   (2) x + 3y = 6
   - Add the equations. The y terms cancel: 5x = 0
   - Divide both sides by 5: x = 0
   - Substitute x = 0 into equation (1): 4(0) − 3y = −6 → −3y = −6 → y = 2
   - Solution (0, 2). Check in equation (2): (0) + 3(2) = 6 ✓

**Practice 1.** Solve by elimination:  3x + y = 10  and  2x − y = 0.  
**Answer: (2, 4)**
   - Line up the equations in standard form:  (1) 3x + y = 10   (2) 2x − y = 0
   - Add the equations. The y terms cancel: 5x = 10
   - Divide both sides by 5: x = 2
   - Substitute x = 2 into equation (1): 3(2) + y = 10 → y = 4
   - Solution (2, 4). Check in equation (2): 2(2) − (4) = 0 ✓

**Practice 2.** Solve by elimination:  −5x + 2y = 1  and  5x + 4y = 17.  
**Answer: (1, 3)**
   - Line up the equations in standard form:  (1) −5x + 2y = 1   (2) 5x + 4y = 17
   - Add the equations. The x terms cancel: 6y = 18
   - Divide both sides by 6: y = 3
   - Substitute y = 3 into equation (1): −5x + 2(3) = 1 → −5x = −5 → x = 1
   - Solution (1, 3). Check in equation (2): 5(1) + 4(3) = 17 ✓

**Practice 3.** Solve by elimination:  x − 6y = −3  and  2x + 6y = 12.  
**Answer: (3, 1)**
   - Line up the equations in standard form:  (1) x − 6y = −3   (2) 2x + 6y = 12
   - Add the equations. The y terms cancel: 3x = 9
   - Divide both sides by 3: x = 3
   - Substitute x = 3 into equation (1): (3) − 6y = −3 → −6y = −6 → y = 1
   - Solution (3, 1). Check in equation (2): 2(3) + 6(1) = 12 ✓

**Practice 4.** Solve by elimination:  7x + 3y = 5  and  −7x + 2y = 15.  
**Answer: (−1, 4)**
   - Line up the equations in standard form:  (1) 7x + 3y = 5   (2) −7x + 2y = 15
   - Add the equations. The x terms cancel: 5y = 20
   - Divide both sides by 5: y = 4
   - Substitute y = 4 into equation (1): 7x + 3(4) = 5 → 7x = −7 → x = −1
   - Solution (−1, 4). Check in equation (2): −7(−1) + 2(4) = 15 ✓

**Practice 5.** Solve by elimination:  2x − 5y = 0  and  3x + 5y = 25.  
**Answer: (5, 2)**
   - Line up the equations in standard form:  (1) 2x − 5y = 0   (2) 3x + 5y = 25
   - Add the equations. The y terms cancel: 5x = 25
   - Divide both sides by 5: x = 5
   - Substitute x = 5 into equation (1): 2(5) − 5y = 0 → −5y = −10 → y = 2
   - Solution (5, 2). Check in equation (2): 3(5) + 5(2) = 25 ✓

**Practice 6.** Solve by elimination:  −4x + y = 5  and  4x + 3y = −17.  
**Answer: (−2, −3)**
   - Line up the equations in standard form:  (1) −4x + y = 5   (2) 4x + 3y = −17
   - Add the equations. The x terms cancel: 4y = −12
   - Divide both sides by 4: y = −3
   - Substitute y = −3 into equation (1): −4x + (−3) = 5 → −4x = 8 → x = −2
   - Solution (−2, −3). Check in equation (2): 4(−2) + 3(−3) = −17 ✓

**Exit 1.** Solve by elimination:  5x + 2y = 9  and  3x − 2y = −1.  
**Answer: (1, 2)**
   - Line up the equations in standard form:  (1) 5x + 2y = 9   (2) 3x − 2y = −1
   - Add the equations. The y terms cancel: 8x = 8
   - Divide both sides by 8: x = 1
   - Substitute x = 1 into equation (1): 5(1) + 2y = 9 → 2y = 4 → y = 2
   - Solution (1, 2). Check in equation (2): 3(1) − 2(2) = −1 ✓

**Exit 2.** Solve by elimination:  −3x + 4y = 2  and  3x + y = 8.  
**Answer: (2, 2)**
   - Line up the equations in standard form:  (1) −3x + 4y = 2   (2) 3x + y = 8
   - Add the equations. The x terms cancel: 5y = 10
   - Divide both sides by 5: y = 2
   - Substitute y = 2 into equation (1): −3x + 4(2) = 2 → −3x = −6 → x = 2
   - Solution (2, 2). Check in equation (2): 3(2) + (2) = 8 ✓

---

## Day 12: Wednesday, January 20: Elimination by multiplying one equation

**Learning target:** I can multiply one equation by a number so that a variable cancels, then solve the system.  
**Standards:** HSA-REI.C.5, HSA-REI.C.6 (full text in the calendar)  
**Materials:** Do Now slide or board, guided notes handout, practice handout, exit ticket slips

### Run of show (50 minutes)

| Time | Segment | Notes |
|---|---|---|
| 0:00-0:07 | Do Now (silent, independent) | Problems on the board; answers in the key. Go over 1-2 quickly. |
| 0:07-0:20 | Mini-lesson: worked examples + find the mistake | Script below. Students copy the examples into their notes. |
| 0:20-0:30 | Guided practice (we do) | Do problem 1 together; students do 2-3 with a partner, then check on whiteboards or by showing work. |
| 0:30-0:45 | Independent practice (you do) | Circulate. See students on the support list first. Early finishers: challenge or next problems. |
| 0:45-0:50 | Exit ticket | Silent. Collect at the door and sort into got it / nearly / not yet. |

### Opening (say this)

"What if nothing cancels? In 2x + y = 7 and 3x − 2y = 0, the y's are +y and −2y. If we multiply the whole first equation by 2, we get +2y, which cancels with −2y. Multiplying both sides of an equation by the same number keeps it true."

### Do Now

1. Solve by elimination:  x + 2y = 5  and  x − 2y = 1.
2. Solve by substitution:  x − y = 2  and  2x + 3y = 4.

### Mini-lesson: worked examples (script)

**Worked example 1:** Solve by elimination:  2x + y = 7  and  3x − 2y = 0.

Write each step on the board and say what you're doing and why. Ask the question in italics before writing the step and give 3-5 seconds of think time.

1. Line up the equations in standard form:  (1) 2x + y = 7   (2) 3x − 2y = 0
2. Multiply EVERY term of equation (1) by 2: 4x + 2y = 14
3. Add the equations. The y terms cancel: 7x = 14
4. Divide both sides by 7: x = 2
5. Substitute x = 2 into equation (1): 2(2) + y = 7 → y = 3
6. Solution (2, 3). Check in equation (2): 3(2) − 2(3) = 0 ✓

Say: *"So the answer is (2, 3). How do we know it's right?"* (We checked it in the original equations.)

**Worked example 2:** Solve by elimination:  3x + 4y = 6  and  x + 2y = 4.

Write each step on the board and say what you're doing and why. Ask the question in italics before writing the step and give 3-5 seconds of think time.

1. Line up the equations in standard form:  (1) 3x + 4y = 6   (2) x + 2y = 4
2. Multiply EVERY term of equation (2) by −2: −2x − 4y = −8
3. Add the equations. The y terms cancel: x = −2
4. Substitute x = −2 into equation (1): 3(−2) + 4y = 6 → 4y = 12 → y = 3
5. Solution (−2, 3). Check in equation (2): (−2) + 2(3) = 4 ✓

Say: *"So the answer is (−2, 3). How do we know it's right?"* (We checked it in the original equations.)

**Find the mistake** (project or write this; ask students to find and explain the error with a partner for 2 minutes):

> Solve: x + 3y = 5 and 2x + 5y = 9 (multiply the first by −2).  
> −2x + 3y = −10  
> Add: 8y = −1  

*What's wrong:* The student only multiplied the x term. EVERY term must be multiplied: −2x − 6y = −10.  
*Correct:* Add: −y = −1, y = 1, x = 2. Solution (2, 1).

### Watch for (common mistakes and what to say)

- **Multiplying only one term.** Say: "Put the whole equation in a box. Everything in the box gets multiplied."
- **Choosing a multiplier that doesn't create opposites.** Say: "We want the coefficients to be opposites, like 4 and −4."

### Guided practice

1. Solve by elimination:  x + y = 7  and  3x + 2y = 19.
2. Solve by elimination:  4x − 3y = 6  and  2x + y = 8.
3. Solve by elimination:  5x + 2y = 3  and  x − y = −5.

### Independent practice

1. Solve by elimination:  2x + 3y = 3  and  x − y = 4.
2. Solve by elimination:  3x + y = 11  and  5x + 2y = 20.
3. Solve by elimination:  x + 4y = 2  and  3x − 2y = −8.
4. Solve by elimination:  6x + 5y = 15  and  3x + 2y = 6.
5. Solve by elimination:  2x − y = 10  and  5x + 3y = 14.
6. Solve by elimination:  7x + 2y = 1  and  x + y = −2.

### Exit ticket

1. Solve by elimination:  3x + 2y = 10  and  x + y = 3.
2. Solve by elimination:  2x + 5y = 4  and  4x − y = −14.

**Sorting:** all correct = *got it* (start tomorrow's Do Now normally); one error = *nearly* (hand back with a hint tomorrow); both wrong or blank = *not yet* (sit with these students during tomorrow's guided practice). Record counts in the handoff log.

### Answer key (fully worked)

**Do Now 1.** Solve by elimination:  x + 2y = 5  and  x − 2y = 1.  
**Answer: (3, 1)**
   - Line up the equations in standard form:  (1) x + 2y = 5   (2) x − 2y = 1
   - Add the equations. The y terms cancel: 2x = 6
   - Divide both sides by 2: x = 3
   - Substitute x = 3 into equation (1): (3) + 2y = 5 → 2y = 2 → y = 1
   - Solution (3, 1). Check in equation (2): (3) − 2(1) = 1 ✓

**Do Now 2.** Solve by substitution:  x − y = 2  and  2x + 3y = 4.  
**Answer: (2, 0)**
   - Solve the first equation for x: x − y = 2  →  x = y + 2
   - Substitute (y + 2) for x in the second equation, keeping the parentheses: 2(y + 2) + 3y = 4
   - Distribute: 2y + 4 + 3y = 4
   - Combine like terms: 5y + 4 = 4
   - Subtract 4 from both sides: 5y = 0
   - Divide both sides by 5: y = 0
   - Substitute y = 0 into x = y + 2: x = (0) + 2 = 2
   - Solution (2, 0). Check in the second equation: 2(2) + 3(0) = 4 ✓

**Example 1.** Solve by elimination:  2x + y = 7  and  3x − 2y = 0.  
**Answer: (2, 3)**
   - Line up the equations in standard form:  (1) 2x + y = 7   (2) 3x − 2y = 0
   - Multiply EVERY term of equation (1) by 2: 4x + 2y = 14
   - Add the equations. The y terms cancel: 7x = 14
   - Divide both sides by 7: x = 2
   - Substitute x = 2 into equation (1): 2(2) + y = 7 → y = 3
   - Solution (2, 3). Check in equation (2): 3(2) − 2(3) = 0 ✓

**Example 2.** Solve by elimination:  3x + 4y = 6  and  x + 2y = 4.  
**Answer: (−2, 3)**
   - Line up the equations in standard form:  (1) 3x + 4y = 6   (2) x + 2y = 4
   - Multiply EVERY term of equation (2) by −2: −2x − 4y = −8
   - Add the equations. The y terms cancel: x = −2
   - Substitute x = −2 into equation (1): 3(−2) + 4y = 6 → 4y = 12 → y = 3
   - Solution (−2, 3). Check in equation (2): (−2) + 2(3) = 4 ✓

**Guided 1.** Solve by elimination:  x + y = 7  and  3x + 2y = 19.  
**Answer: (5, 2)**
   - Line up the equations in standard form:  (1) x + y = 7   (2) 3x + 2y = 19
   - Multiply EVERY term of equation (1) by 2: 2x + 2y = 14
   - Multiply EVERY term of equation (2) by −1: −3x − 2y = −19
   - Add the equations. The y terms cancel: −x = −5
   - Divide both sides by −1: x = 5
   - Substitute x = 5 into equation (1): (5) + y = 7 → y = 2
   - Solution (5, 2). Check in equation (2): 3(5) + 2(2) = 19 ✓

**Guided 2.** Solve by elimination:  4x − 3y = 6  and  2x + y = 8.  
**Answer: (3, 2)**
   - Line up the equations in standard form:  (1) 4x − 3y = 6   (2) 2x + y = 8
   - Multiply EVERY term of equation (2) by −2: −4x − 2y = −16
   - Add the equations. The x terms cancel: −5y = −10
   - Divide both sides by −5: y = 2
   - Substitute y = 2 into equation (1): 4x − 3(2) = 6 → 4x = 12 → x = 3
   - Solution (3, 2). Check in equation (2): 2(3) + (2) = 8 ✓

**Guided 3.** Solve by elimination:  5x + 2y = 3  and  x − y = −5.  
**Answer: (−1, 4)**
   - Line up the equations in standard form:  (1) 5x + 2y = 3   (2) x − y = −5
   - Multiply EVERY term of equation (2) by 2: 2x − 2y = −10
   - Add the equations. The y terms cancel: 7x = −7
   - Divide both sides by 7: x = −1
   - Substitute x = −1 into equation (1): 5(−1) + 2y = 3 → 2y = 8 → y = 4
   - Solution (−1, 4). Check in equation (2): (−1) − (4) = −5 ✓

**Practice 1.** Solve by elimination:  2x + 3y = 3  and  x − y = 4.  
**Answer: (3, −1)**
   - Line up the equations in standard form:  (1) 2x + 3y = 3   (2) x − y = 4
   - Multiply EVERY term of equation (2) by −2: −2x + 2y = −8
   - Add the equations. The x terms cancel: 5y = −5
   - Divide both sides by 5: y = −1
   - Substitute y = −1 into equation (1): 2x + 3(−1) = 3 → 2x = 6 → x = 3
   - Solution (3, −1). Check in equation (2): (3) − (−1) = 4 ✓

**Practice 2.** Solve by elimination:  3x + y = 11  and  5x + 2y = 20.  
**Answer: (2, 5)**
   - Line up the equations in standard form:  (1) 3x + y = 11   (2) 5x + 2y = 20
   - Multiply EVERY term of equation (1) by 2: 6x + 2y = 22
   - Multiply EVERY term of equation (2) by −1: −5x − 2y = −20
   - Add the equations. The y terms cancel: x = 2
   - Substitute x = 2 into equation (1): 3(2) + y = 11 → y = 5
   - Solution (2, 5). Check in equation (2): 5(2) + 2(5) = 20 ✓

**Practice 3.** Solve by elimination:  x + 4y = 2  and  3x − 2y = −8.  
**Answer: (−2, 1)**
   - Line up the equations in standard form:  (1) x + 4y = 2   (2) 3x − 2y = −8
   - Multiply EVERY term of equation (2) by 2: 6x − 4y = −16
   - Add the equations. The y terms cancel: 7x = −14
   - Divide both sides by 7: x = −2
   - Substitute x = −2 into equation (1): (−2) + 4y = 2 → 4y = 4 → y = 1
   - Solution (−2, 1). Check in equation (2): 3(−2) − 2(1) = −8 ✓

**Practice 4.** Solve by elimination:  6x + 5y = 15  and  3x + 2y = 6.  
**Answer: (0, 3)**
   - Line up the equations in standard form:  (1) 6x + 5y = 15   (2) 3x + 2y = 6
   - Multiply EVERY term of equation (2) by −2: −6x − 4y = −12
   - Add the equations. The x terms cancel: y = 3
   - Substitute y = 3 into equation (1): 6x + 5(3) = 15 → 6x = 0 → x = 0
   - Solution (0, 3). Check in equation (2): 3(0) + 2(3) = 6 ✓

**Practice 5.** Solve by elimination:  2x − y = 10  and  5x + 3y = 14.  
**Answer: (4, −2)**
   - Line up the equations in standard form:  (1) 2x − y = 10   (2) 5x + 3y = 14
   - Multiply EVERY term of equation (1) by 3: 6x − 3y = 30
   - Add the equations. The y terms cancel: 11x = 44
   - Divide both sides by 11: x = 4
   - Substitute x = 4 into equation (1): 2(4) − y = 10 → −y = 2 → y = −2
   - Solution (4, −2). Check in equation (2): 5(4) + 3(−2) = 14 ✓

**Practice 6.** Solve by elimination:  7x + 2y = 1  and  x + y = −2.  
**Answer: (1, −3)**
   - Line up the equations in standard form:  (1) 7x + 2y = 1   (2) x + y = −2
   - Multiply EVERY term of equation (2) by −2: −2x − 2y = 4
   - Add the equations. The y terms cancel: 5x = 5
   - Divide both sides by 5: x = 1
   - Substitute x = 1 into equation (1): 7(1) + 2y = 1 → 2y = −6 → y = −3
   - Solution (1, −3). Check in equation (2): (1) + (−3) = −2 ✓

**Exit 1.** Solve by elimination:  3x + 2y = 10  and  x + y = 3.  
**Answer: (4, −1)**
   - Line up the equations in standard form:  (1) 3x + 2y = 10   (2) x + y = 3
   - Multiply EVERY term of equation (2) by −2: −2x − 2y = −6
   - Add the equations. The y terms cancel: x = 4
   - Substitute x = 4 into equation (1): 3(4) + 2y = 10 → 2y = −2 → y = −1
   - Solution (4, −1). Check in equation (2): (4) + (−1) = 3 ✓

**Exit 2.** Solve by elimination:  2x + 5y = 4  and  4x − y = −14.  
**Answer: (−3, 2)**
   - Line up the equations in standard form:  (1) 2x + 5y = 4   (2) 4x − y = −14
   - Multiply EVERY term of equation (1) by 2: 4x + 10y = 8
   - Multiply EVERY term of equation (2) by −1: −4x + y = 14
   - Add the equations. The x terms cancel: 11y = 22
   - Divide both sides by 11: y = 2
   - Substitute y = 2 into equation (1): 2x + 5(2) = 4 → 2x = −6 → x = −3
   - Solution (−3, 2). Check in equation (2): 4(−3) − (2) = −14 ✓

---

## Day 13: Thursday, January 21: Elimination by multiplying both equations

**Learning target:** I can multiply both equations so a variable cancels, then solve the system.  
**Standards:** HSA-REI.C.5, HSA-REI.C.6 (full text in the calendar)  
**Materials:** Do Now slide or board, guided notes handout, practice handout, exit ticket slips

### Run of show (50 minutes)

| Time | Segment | Notes |
|---|---|---|
| 0:00-0:07 | Do Now (silent, independent) | Problems on the board; answers in the key. Go over 1-2 quickly. |
| 0:07-0:20 | Mini-lesson: worked examples + find the mistake | Script below. Students copy the examples into their notes. |
| 0:20-0:30 | Guided practice (we do) | Do problem 1 together; students do 2-3 with a partner, then check on whiteboards or by showing work. |
| 0:30-0:45 | Independent practice (you do) | Circulate. See students on the support list first. Early finishers: challenge or next problems. |
| 0:45-0:50 | Exit ticket | Silent. Collect at the door and sort into got it / nearly / not yet. |

### Opening (say this)

"Sometimes no single multiplier works, like 3x + 4y = 10 and 2x + 3y = 7. Find the least common multiple of the coefficients of one variable and multiply both equations to get opposites, like +6x and −6x."

### Do Now

1. Solve by elimination:  2x + y = 5  and  3x − y = 0.
2. Solve by elimination:  x + 2y = 2  and  3x + 5y = 7.

### Mini-lesson: worked examples (script)

**Worked example 1:** Solve by elimination:  3x + 4y = 10  and  2x + 3y = 7.

Write each step on the board and say what you're doing and why. Ask the question in italics before writing the step and give 3-5 seconds of think time.

1. Line up the equations in standard form:  (1) 3x + 4y = 10   (2) 2x + 3y = 7
2. Multiply EVERY term of equation (1) by 2: 6x + 8y = 20
3. Multiply EVERY term of equation (2) by −3: −6x − 9y = −21
4. Add the equations. The x terms cancel: −y = −1
5. Divide both sides by −1: y = 1
6. Substitute y = 1 into equation (1): 3x + 4(1) = 10 → 3x = 6 → x = 2
7. Solution (2, 1). Check in equation (2): 2(2) + 3(1) = 7 ✓

Say: *"So the answer is (2, 1). How do we know it's right?"* (We checked it in the original equations.)

**Worked example 2:** Solve by elimination:  5x + 3y = 4  and  4x − 2y = −10.

Write each step on the board and say what you're doing and why. Ask the question in italics before writing the step and give 3-5 seconds of think time.

1. Line up the equations in standard form:  (1) 5x + 3y = 4   (2) 4x − 2y = −10
2. Multiply EVERY term of equation (1) by 2: 10x + 6y = 8
3. Multiply EVERY term of equation (2) by 3: 12x − 6y = −30
4. Add the equations. The y terms cancel: 22x = −22
5. Divide both sides by 22: x = −1
6. Substitute x = −1 into equation (1): 5(−1) + 3y = 4 → 3y = 9 → y = 3
7. Solution (−1, 3). Check in equation (2): 4(−1) − 2(3) = −10 ✓

Say: *"So the answer is (−1, 3). How do we know it's right?"* (We checked it in the original equations.)

**Find the mistake** (project or write this; ask students to find and explain the error with a partner for 2 minutes):

> Solve: 2x + 3y = 12 and 5x − 2y = 11 (eliminate y).  
> Multiply (1) by 2: 4x + 6y = 24  
> Multiply (2) by 3: 15x − 6y = 11  
> Add: 19x = 35  

*What's wrong:* The right side of equation (2) wasn't multiplied: 3 × 11 = 33.  
*Correct:* 19x = 57, x = 3, y = 2. Solution (3, 2).

### Watch for (common mistakes and what to say)

- **Forgetting to multiply the constant.** Say: "Box it, multiply everything in the box."
- **Sign errors when multiplying by a negative.** Say: "Say the sign out loud: negative times negative is positive."
- **Picking a harder variable.** Say: "Look at the coefficients. Which pair has the smaller least common multiple?"

### Guided practice

1. Solve by elimination:  2x + 3y = 8  and  3x + 5y = 13.
2. Solve by elimination:  4x + 3y = 6  and  3x − 2y = 13.
3. Solve by elimination:  5x + 2y = 8  and  3x − 5y = 11.

### Independent practice

1. Solve by elimination:  3x + 5y = 7  and  2x + 3y = 4.
2. Solve by elimination:  4x − 3y = 1  and  6x + 5y = 11.
3. Solve by elimination:  2x + 7y = 1  and  3x − 4y = 16.
4. Solve by elimination:  5x + 4y = −2  and  3x + 6y = −12.
5. Solve by elimination:  7x + 3y = 15  and  5x + 2y = 10.
6. Solve by elimination:  3x + 4y = 5  and  5x + 6y = 8.

### Exit ticket

1. Solve by elimination:  3x + 2y = 6  and  2x + 5y = −7.
2. Solve by elimination:  4x + 5y = 6  and  6x − 7y = −20.

**Sorting:** all correct = *got it* (start tomorrow's Do Now normally); one error = *nearly* (hand back with a hint tomorrow); both wrong or blank = *not yet* (sit with these students during tomorrow's guided practice). Record counts in the handoff log.

### Answer key (fully worked)

**Do Now 1.** Solve by elimination:  2x + y = 5  and  3x − y = 0.  
**Answer: (1, 3)**
   - Line up the equations in standard form:  (1) 2x + y = 5   (2) 3x − y = 0
   - Add the equations. The y terms cancel: 5x = 5
   - Divide both sides by 5: x = 1
   - Substitute x = 1 into equation (1): 2(1) + y = 5 → y = 3
   - Solution (1, 3). Check in equation (2): 3(1) − (3) = 0 ✓

**Do Now 2.** Solve by elimination:  x + 2y = 2  and  3x + 5y = 7.  
**Answer: (4, −1)**
   - Line up the equations in standard form:  (1) x + 2y = 2   (2) 3x + 5y = 7
   - Multiply EVERY term of equation (1) by 3: 3x + 6y = 6
   - Multiply EVERY term of equation (2) by −1: −3x − 5y = −7
   - Add the equations. The x terms cancel: y = −1
   - Substitute y = −1 into equation (1): x + 2(−1) = 2 → x = 4
   - Solution (4, −1). Check in equation (2): 3(4) + 5(−1) = 7 ✓

**Example 1.** Solve by elimination:  3x + 4y = 10  and  2x + 3y = 7.  
**Answer: (2, 1)**
   - Line up the equations in standard form:  (1) 3x + 4y = 10   (2) 2x + 3y = 7
   - Multiply EVERY term of equation (1) by 2: 6x + 8y = 20
   - Multiply EVERY term of equation (2) by −3: −6x − 9y = −21
   - Add the equations. The x terms cancel: −y = −1
   - Divide both sides by −1: y = 1
   - Substitute y = 1 into equation (1): 3x + 4(1) = 10 → 3x = 6 → x = 2
   - Solution (2, 1). Check in equation (2): 2(2) + 3(1) = 7 ✓

**Example 2.** Solve by elimination:  5x + 3y = 4  and  4x − 2y = −10.  
**Answer: (−1, 3)**
   - Line up the equations in standard form:  (1) 5x + 3y = 4   (2) 4x − 2y = −10
   - Multiply EVERY term of equation (1) by 2: 10x + 6y = 8
   - Multiply EVERY term of equation (2) by 3: 12x − 6y = −30
   - Add the equations. The y terms cancel: 22x = −22
   - Divide both sides by 22: x = −1
   - Substitute x = −1 into equation (1): 5(−1) + 3y = 4 → 3y = 9 → y = 3
   - Solution (−1, 3). Check in equation (2): 4(−1) − 2(3) = −10 ✓

**Guided 1.** Solve by elimination:  2x + 3y = 8  and  3x + 5y = 13.  
**Answer: (1, 2)**
   - Line up the equations in standard form:  (1) 2x + 3y = 8   (2) 3x + 5y = 13
   - Multiply EVERY term of equation (1) by 3: 6x + 9y = 24
   - Multiply EVERY term of equation (2) by −2: −6x − 10y = −26
   - Add the equations. The x terms cancel: −y = −2
   - Divide both sides by −1: y = 2
   - Substitute y = 2 into equation (1): 2x + 3(2) = 8 → 2x = 2 → x = 1
   - Solution (1, 2). Check in equation (2): 3(1) + 5(2) = 13 ✓

**Guided 2.** Solve by elimination:  4x + 3y = 6  and  3x − 2y = 13.  
**Answer: (3, −2)**
   - Line up the equations in standard form:  (1) 4x + 3y = 6   (2) 3x − 2y = 13
   - Multiply EVERY term of equation (1) by 2: 8x + 6y = 12
   - Multiply EVERY term of equation (2) by 3: 9x − 6y = 39
   - Add the equations. The y terms cancel: 17x = 51
   - Divide both sides by 17: x = 3
   - Substitute x = 3 into equation (1): 4(3) + 3y = 6 → 3y = −6 → y = −2
   - Solution (3, −2). Check in equation (2): 3(3) − 2(−2) = 13 ✓

**Guided 3.** Solve by elimination:  5x + 2y = 8  and  3x − 5y = 11.  
**Answer: (2, −1)**
   - Line up the equations in standard form:  (1) 5x + 2y = 8   (2) 3x − 5y = 11
   - Multiply EVERY term of equation (1) by 5: 25x + 10y = 40
   - Multiply EVERY term of equation (2) by 2: 6x − 10y = 22
   - Add the equations. The y terms cancel: 31x = 62
   - Divide both sides by 31: x = 2
   - Substitute x = 2 into equation (1): 5(2) + 2y = 8 → 2y = −2 → y = −1
   - Solution (2, −1). Check in equation (2): 3(2) − 5(−1) = 11 ✓

**Practice 1.** Solve by elimination:  3x + 5y = 7  and  2x + 3y = 4.  
**Answer: (−1, 2)**
   - Line up the equations in standard form:  (1) 3x + 5y = 7   (2) 2x + 3y = 4
   - Multiply EVERY term of equation (1) by 2: 6x + 10y = 14
   - Multiply EVERY term of equation (2) by −3: −6x − 9y = −12
   - Add the equations. The x terms cancel: y = 2
   - Substitute y = 2 into equation (1): 3x + 5(2) = 7 → 3x = −3 → x = −1
   - Solution (−1, 2). Check in equation (2): 2(−1) + 3(2) = 4 ✓

**Practice 2.** Solve by elimination:  4x − 3y = 1  and  6x + 5y = 11.  
**Answer: (1, 1)**
   - Line up the equations in standard form:  (1) 4x − 3y = 1   (2) 6x + 5y = 11
   - Multiply EVERY term of equation (1) by 3: 12x − 9y = 3
   - Multiply EVERY term of equation (2) by −2: −12x − 10y = −22
   - Add the equations. The x terms cancel: −19y = −19
   - Divide both sides by −19: y = 1
   - Substitute y = 1 into equation (1): 4x − 3(1) = 1 → 4x = 4 → x = 1
   - Solution (1, 1). Check in equation (2): 6(1) + 5(1) = 11 ✓

**Practice 3.** Solve by elimination:  2x + 7y = 1  and  3x − 4y = 16.  
**Answer: (4, −1)**
   - Line up the equations in standard form:  (1) 2x + 7y = 1   (2) 3x − 4y = 16
   - Multiply EVERY term of equation (1) by 3: 6x + 21y = 3
   - Multiply EVERY term of equation (2) by −2: −6x + 8y = −32
   - Add the equations. The x terms cancel: 29y = −29
   - Divide both sides by 29: y = −1
   - Substitute y = −1 into equation (1): 2x + 7(−1) = 1 → 2x = 8 → x = 4
   - Solution (4, −1). Check in equation (2): 3(4) − 4(−1) = 16 ✓

**Practice 4.** Solve by elimination:  5x + 4y = −2  and  3x + 6y = −12.  
**Answer: (2, −3)**
   - Line up the equations in standard form:  (1) 5x + 4y = −2   (2) 3x + 6y = −12
   - Multiply EVERY term of equation (1) by 3: 15x + 12y = −6
   - Multiply EVERY term of equation (2) by −2: −6x − 12y = 24
   - Add the equations. The y terms cancel: 9x = 18
   - Divide both sides by 9: x = 2
   - Substitute x = 2 into equation (1): 5(2) + 4y = −2 → 4y = −12 → y = −3
   - Solution (2, −3). Check in equation (2): 3(2) + 6(−3) = −12 ✓

**Practice 5.** Solve by elimination:  7x + 3y = 15  and  5x + 2y = 10.  
**Answer: (0, 5)**
   - Line up the equations in standard form:  (1) 7x + 3y = 15   (2) 5x + 2y = 10
   - Multiply EVERY term of equation (1) by 2: 14x + 6y = 30
   - Multiply EVERY term of equation (2) by −3: −15x − 6y = −30
   - Add the equations. The y terms cancel: −x = 0
   - Divide both sides by −1: x = 0
   - Substitute x = 0 into equation (1): 7(0) + 3y = 15 → 3y = 15 → y = 5
   - Solution (0, 5). Check in equation (2): 5(0) + 2(5) = 10 ✓

**Practice 6.** Solve by elimination:  3x + 4y = 5  and  5x + 6y = 8.  
**Answer: (1, 1/2)**
   - Line up the equations in standard form:  (1) 3x + 4y = 5   (2) 5x + 6y = 8
   - Multiply EVERY term of equation (1) by 3: 9x + 12y = 15
   - Multiply EVERY term of equation (2) by −2: −10x − 12y = −16
   - Add the equations. The y terms cancel: −x = −1
   - Divide both sides by −1: x = 1
   - Substitute x = 1 into equation (1): 3(1) + 4y = 5 → 4y = 2 → y = 1/2
   - Solution (1, 1/2). Check in equation (2): 5(1) + 6(1/2) = 8 ✓

**Exit 1.** Solve by elimination:  3x + 2y = 6  and  2x + 5y = −7.  
**Answer: (4, −3)**
   - Line up the equations in standard form:  (1) 3x + 2y = 6   (2) 2x + 5y = −7
   - Multiply EVERY term of equation (1) by 2: 6x + 4y = 12
   - Multiply EVERY term of equation (2) by −3: −6x − 15y = 21
   - Add the equations. The x terms cancel: −11y = 33
   - Divide both sides by −11: y = −3
   - Substitute y = −3 into equation (1): 3x + 2(−3) = 6 → 3x = 12 → x = 4
   - Solution (4, −3). Check in equation (2): 2(4) + 5(−3) = −7 ✓

**Exit 2.** Solve by elimination:  4x + 5y = 6  and  6x − 7y = −20.  
**Answer: (−1, 2)**
   - Line up the equations in standard form:  (1) 4x + 5y = 6   (2) 6x − 7y = −20
   - Multiply EVERY term of equation (1) by 3: 12x + 15y = 18
   - Multiply EVERY term of equation (2) by −2: −12x + 14y = 40
   - Add the equations. The x terms cancel: 29y = 58
   - Divide both sides by 29: y = 2
   - Substitute y = 2 into equation (1): 4x + 5(2) = 6 → 4x = −4 → x = −1
   - Solution (−1, 2). Check in equation (2): 6(−1) − 7(2) = −20 ✓

---

## Day 14: Friday, January 22: Choosing a method + mini-quiz

**Learning target:** I can choose an efficient method (graphing, substitution or elimination) and explain my choice.  
**Standards:** HSA-REI.C.6, HSA-REI.C.5 (full text in the calendar)  
**Materials:** Do Now slide or board, guided notes handout, practice handout, exit ticket slips

### Run of show (50 minutes)

| Time | Segment | Notes |
|---|---|---|
| 0:00-0:05 | Do Now | Quick warm-up; go over answers. |
| 0:05-0:10 | Mini-lesson / discussion | See notes below. |
| 0:10-0:30 | Quiz | Silent, individual. Extended time per IEP/504 plans. |
| 0:30-0:50 | Flex / reteach | See the flex plan below. |

### Opening (say this)

"This week lost a day to the holiday, so today combines practice and a short quiz. All three methods give the same answer; the skill is choosing the fastest one. A variable already alone or with coefficient 1: substitution. Opposite or matching coefficients: elimination. Want a quick picture or estimate: graphing."

### Do Now

1. Solve by elimination:  x + y = 5  and  2x − y = 4.
2. Solve by substitution:  y = 2x − 1  and  3x + y = 4.

### Mini-lesson: worked examples (script)

**Worked example 1:** Solve by substitution:  y = −x + 5  and  2x + 3y = 12.

Write each step on the board and say what you're doing and why. Ask the question in italics before writing the step and give 3-5 seconds of think time.

1. The first equation already says y = −x + 5.
2. Substitute (−x + 5) for y in the second equation, keeping the parentheses: 2x + 3(−x + 5) = 12
3. Distribute: 2x − 3x + 15 = 12
4. Combine like terms: −x + 15 = 12
5. Subtract 15 from both sides: −x = −3
6. Divide both sides by −1: x = 3
7. Substitute x = 3 into y = −x + 5: y = −(3) + 5 = 2
8. Solution (3, 2). Check in the second equation: 2(3) + 3(2) = 12 ✓

Say: *"So the answer is (3, 2). How do we know it's right?"* (We checked it in the original equations.)

**Worked example 2:** Solve by elimination:  4x + 3y = 5  and  2x − 3y = 7.

Write each step on the board and say what you're doing and why. Ask the question in italics before writing the step and give 3-5 seconds of think time.

1. Line up the equations in standard form:  (1) 4x + 3y = 5   (2) 2x − 3y = 7
2. Add the equations. The y terms cancel: 6x = 12
3. Divide both sides by 6: x = 2
4. Substitute x = 2 into equation (1): 4(2) + 3y = 5 → 3y = −3 → y = −1
5. Solution (2, −1). Check in equation (2): 2(2) − 3(−1) = 7 ✓

Say: *"So the answer is (2, −1). How do we know it's right?"* (We checked it in the original equations.)

### Quiz (print separately)

1. Solve by elimination:  3x + 2y = 11  and  5x − 2y = −3.
2. Solve by elimination:  2x + 3y = 7  and  3x + 2y = 3.
3. Solve by substitution:  x − 4y = 2  and  3x + 5y = 6.
4. Solve by elimination:  2x − 3y = 5  and  −4x + 6y = −10.
5. Solve by elimination:  3x + y = 4  and  6x + 2y = 5.

**Choosing a method — discuss before the quiz (10 minutes):** show the three systems below and have students vote with fingers (1 = graphing, 2 = substitution, 3 = elimination), then explain their choice to a partner. There is no single right answer; the explanation matters.

- y = 4x − 1 and 3x + 2y = 9 (substitution: y is already alone)
- 5x + 3y = 7 and 2x − 3y = 7 (elimination: +3y and −3y)
- y = x + 2 and y = −x + 4 (graphing works nicely: simple lines)

### Answer key (fully worked)

**Do Now 1.** Solve by elimination:  x + y = 5  and  2x − y = 4.  
**Answer: (3, 2)**
   - Line up the equations in standard form:  (1) x + y = 5   (2) 2x − y = 4
   - Add the equations. The y terms cancel: 3x = 9
   - Divide both sides by 3: x = 3
   - Substitute x = 3 into equation (1): (3) + y = 5 → y = 2
   - Solution (3, 2). Check in equation (2): 2(3) − (2) = 4 ✓

**Do Now 2.** Solve by substitution:  y = 2x − 1  and  3x + y = 4.  
**Answer: (1, 1)**
   - The first equation already says y = 2x − 1.
   - Substitute (2x − 1) for y in the second equation, keeping the parentheses: 3x + (2x − 1) = 4
   - Distribute: 3x + 2x − 1 = 4
   - Combine like terms: 5x − 1 = 4
   - Add 1 to both sides: 5x = 5
   - Divide both sides by 5: x = 1
   - Substitute x = 1 into y = 2x − 1: y = 2(1) − 1 = 1
   - Solution (1, 1). Check in the second equation: 3(1) + (1) = 4 ✓

**Example 1.** Solve by substitution:  y = −x + 5  and  2x + 3y = 12.  
**Answer: (3, 2)**
   - The first equation already says y = −x + 5.
   - Substitute (−x + 5) for y in the second equation, keeping the parentheses: 2x + 3(−x + 5) = 12
   - Distribute: 2x − 3x + 15 = 12
   - Combine like terms: −x + 15 = 12
   - Subtract 15 from both sides: −x = −3
   - Divide both sides by −1: x = 3
   - Substitute x = 3 into y = −x + 5: y = −(3) + 5 = 2
   - Solution (3, 2). Check in the second equation: 2(3) + 3(2) = 12 ✓

**Example 2.** Solve by elimination:  4x + 3y = 5  and  2x − 3y = 7.  
**Answer: (2, −1)**
   - Line up the equations in standard form:  (1) 4x + 3y = 5   (2) 2x − 3y = 7
   - Add the equations. The y terms cancel: 6x = 12
   - Divide both sides by 6: x = 2
   - Substitute x = 2 into equation (1): 4(2) + 3y = 5 → 3y = −3 → y = −1
   - Solution (2, −1). Check in equation (2): 2(2) − 3(−1) = 7 ✓

**Quiz 1.** Solve by elimination:  3x + 2y = 11  and  5x − 2y = −3.  
**Answer: (1, 4)**
   - Line up the equations in standard form:  (1) 3x + 2y = 11   (2) 5x − 2y = −3
   - Add the equations. The y terms cancel: 8x = 8
   - Divide both sides by 8: x = 1
   - Substitute x = 1 into equation (1): 3(1) + 2y = 11 → 2y = 8 → y = 4
   - Solution (1, 4). Check in equation (2): 5(1) − 2(4) = −3 ✓

**Quiz 2.** Solve by elimination:  2x + 3y = 7  and  3x + 2y = 3.  
**Answer: (−1, 3)**
   - Line up the equations in standard form:  (1) 2x + 3y = 7   (2) 3x + 2y = 3
   - Multiply EVERY term of equation (1) by 2: 4x + 6y = 14
   - Multiply EVERY term of equation (2) by −3: −9x − 6y = −9
   - Add the equations. The y terms cancel: −5x = 5
   - Divide both sides by −5: x = −1
   - Substitute x = −1 into equation (1): 2(−1) + 3y = 7 → 3y = 9 → y = 3
   - Solution (−1, 3). Check in equation (2): 3(−1) + 2(3) = 3 ✓

**Quiz 3.** Solve by substitution:  x − 4y = 2  and  3x + 5y = 6.  
**Answer: (2, 0)**
   - Solve the first equation for x: x − 4y = 2  →  x = 4y + 2
   - Substitute (4y + 2) for x in the second equation, keeping the parentheses: 3(4y + 2) + 5y = 6
   - Distribute: 12y + 6 + 5y = 6
   - Combine like terms: 17y + 6 = 6
   - Subtract 6 from both sides: 17y = 0
   - Divide both sides by 17: y = 0
   - Substitute y = 0 into x = 4y + 2: x = 4(0) + 2 = 2
   - Solution (2, 0). Check in the second equation: 3(2) + 5(0) = 6 ✓

**Quiz 4.** Solve by elimination:  2x − 3y = 5  and  −4x + 6y = −10.  
**Answer: infinitely many solutions**
   - Line up the equations in standard form:  (1) 2x − 3y = 5   (2) −4x + 6y = −10
   - Multiply EVERY term of equation (1) by 2: 4x − 6y = 10
   - Add the equations: both variables cancel, leaving 0 = 0.
   - 0 = 0 is always true: infinitely many solutions (same line).

**Quiz 5.** Solve by elimination:  3x + y = 4  and  6x + 2y = 5.  
**Answer: no solution**
   - Line up the equations in standard form:  (1) 3x + y = 4   (2) 6x + 2y = 5
   - Multiply EVERY term of equation (1) by 2: 6x + 2y = 8
   - Multiply EVERY term of equation (2) by −1: −6x − 2y = −5
   - Add the equations: both variables cancel, leaving 0 = 3.
   - 0 = 3 is never true: no solution (parallel lines).

---
