#!/usr/bin/env python3

import mathml_verbosifier

total = 0
failures = 0

test_cases = [
    ("7", "<mn>7</mn>"),
    ("42", "<mn>42</mn>"),
    ("a", "<mi>a</mi>"),
    ("ab", "<mi>a</mi><mi>b</mi>"),
    ("-", "<mo>-</mo>"),
    ("<msup>e -7t</msup>",
     "<msup><mi>e</mi><mrow><mo>-</mo><mn>7</mn><mi>t</mi></mrow></msup>"), 
    ("<mfrac>i(t) c(t)</mfrac>",
     
    "<mfrac>"
     "<mrow><mi>i</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow>"
     "<mrow><mi>c</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow>"
     "</mfrac>"),

    ("<mfrac>i(t-d) c(t)</mfrac>",
     
     "<mfrac>"
     "<mrow><mi>i</mi><mo>(</mo><mi>t</mi><mo>-</mo><mi>d</mi><mo>)</mo></mrow>"
     "<mrow><mi>c</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow>"
     "</mfrac>"),

   ("<mfrac>i(t) c(t)</mfrac>"
     "= k ="
     "<mfrac>"
     "<mrow><mi>ln</mi>(2)</mrow>"
     "<msub>T d</msub>"
     "</mfrac>",
     
     "<mfrac>"
     "<mrow><mi>i</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow>"
     "<mrow><mi>c</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow>"
     "</mfrac>"
     "<mo>=</mo><mi>k</mi><mo>=</mo>"
     "<mfrac>"
     "<mrow><mi>ln</mi><mo>(</mo><mn>2</mn><mo>)</mo></mrow>"
     "<msub><mi>T</mi><mi>d</mi></msub>"
     "</mfrac>"),
    
    ("<mfrac>i(t-d) c(t)</mfrac>"
     "="
     "<mfrac>"
     "<mrow>k<msup>e k(t-d)</msup></mrow>"
     "<msup>e kt</msup>"
     "</mfrac>"
     "= "
     "k"
     "<mfrac><mrow><msup>e kt</msup><msup>e -kd</msup></mrow>"
     "<msup>e kt</msup>"
     "</mfrac>"
     "= "
     "k"
     "<msup>e -kd</msup>"
     "="
     "<mfrac>"
     "<mrow><mi>ln</mi>(2)</mrow>"
     "<msub>T d</msub>"
     "</mfrac>"
     "<msup>"
     "e "
     "<mrow>-<mfrac><mrow><mi>ln</mi>(2)</mrow><msub>T d</msub></mfrac>d</mrow>"
     "</msup>"
     "="
     "<mfrac>"
     "<mrow>2<mi>ln</mi>(2)</mrow>"
     "<msub>T d</msub>"
     "</mfrac>"
     "<msup>e<mfrac>-d <msub>T d</msub></mfrac></msup>",

     "<mfrac>"
     "<mrow><mi>i</mi><mo>(</mo><mi>t</mi><mo>-</mo><mi>d</mi><mo>)</mo></mrow>"
     "<mrow><mi>c</mi><mo>(</mo><mi>t</mi><mo>)</mo></mrow>"
     "</mfrac>"
     "<mo>=</mo>"
     "<mfrac>"
     "<mrow>"
     "<mi>k</mi>"
     "<msup><mi>e</mi>"
     "<mrow><mi>k</mi><mo>(</mo><mi>t</mi><mo>-</mo><mi>d</mi><mo>)</mo>"
     "</mrow></msup></mrow>"
     "<msup><mi>e</mi><mrow><mi>k</mi><mi>t</mi></mrow></msup>"
     "</mfrac>"
     "<mo>=</mo>"
     "<mi>k</mi>"
     "<mfrac><mrow><msup><mi>e</mi><mrow><mi>k</mi><mi>t</mi></mrow></msup>"
     "<msup><mi>e</mi><mrow><mo>-</mo><mi>k</mi><mi>d</mi></mrow></msup>"
     "</mrow>"
     "<msup><mi>e</mi><mrow><mi>k</mi><mi>t</mi></mrow></msup></mfrac>"
     "<mo>=</mo>"
     "<mi>k</mi>"
     "<msup><mi>e</mi><mrow><mo>-</mo><mi>k</mi><mi>d</mi></mrow></msup>"
     "<mo>=</mo>"
     "<mfrac><mrow><mi>ln</mi><mo>(</mo><mn>2</mn><mo>)</mo></mrow>"
     "<msub><mi>T</mi><mi>d</mi></msub></mfrac>"
     "<msup><mi>e</mi><mrow><mo>-</mo><mfrac><mrow><mi>ln</mi>"
     "<mo>(</mo><mn>2</mn><mo>)</mo></mrow><msub><mi>T</mi><mi>d</mi>"
     "</msub></mfrac><mi>d</mi></mrow></msup>"
     "<mo>=</mo><mfrac><mrow><mn>2</mn><mi>ln</mi><mo>(</mo><mn>2</mn><mo>)</mo>"
     "</mrow><msub><mi>T</mi><mi>d</mi></msub></mfrac>"
     "<msup><mi>e</mi><mfrac><mrow><mo>-</mo><mi>d</mi></mrow><msub><mi>T</mi>"
     "<mi>d</mi></msub></mfrac></msup>"
    ),

    ("<msup>a 2</msup> + <msup>b 2</msup> = <msup>c 2</msup>",
     """
         <msup>
           <mi>a</mi>
           <mn>2</mn>
         </msup>
         <mo>+</mo>
         <msup>
           <mi>b</mi>
           <mn>2</mn>
         </msup>
         <mo>=</mo>
         <msup>
           <mi>c</mi>
           <mn>2</mn>
         </msup>
     """),

    ("<mtable>"
     "<mtr>"
     "<mtd><msup>(a+b) 2</msup></mtd>"
     "<mtd>=</mtd>"
     "<mtd><msup>c 2</msup>+4⋅(<mfrac>1 2</mfrac>ab)</mtd>"
     "</mtr>"
     "<mtr>"
     "<mtd><msup>a 2</msup>+2ab+<msup>b 2</msup></mtd>"
     "<mtd>=</mtd>"
     "<mtd><msup>c 2</msup>+2ab</mtd></mtr>"
     "<mtr><mtd><msup>a 2</msup>+<msup>b 2</msup></mtd>"
     "<mtd>=</mtd>"
     "<mtd><msup>c 2</msup></mtd>"
     "</mtr>"
     "</mtable>"
     ,
     
     """
       <mtable>
         <mtr>
           <mtd>
             <msup>
               <mrow>
                 <mo>(</mo>
                 <mi>a</mi>
                 <mo>+</mo>
                 <mi>b</mi>
                 <mo>)</mo>
               </mrow>
               <mn>2</mn>
             </msup>
           </mtd>
           <mtd>
             <mo>=</mo>
           </mtd>
           <mtd>
             <msup>
               <mi>c</mi>
               <mn>2</mn>
             </msup>
             <mo>+</mo>
             <mn>4</mn>
             <mo>⋅</mo>
             <mo>(</mo>
             <mfrac>
               <mn>1</mn>
               <mn>2</mn>
             </mfrac>
             <mi>a</mi>
             <mi>b</mi>
             <mo>)</mo>
           </mtd>
         </mtr>
         <mtr>
           <mtd>
             <msup>
               <mi>a</mi>
               <mn>2</mn>
             </msup>
             <mo>+</mo>
             <mn>2</mn>
             <mi>a</mi>
             <mi>b</mi>
             <mo>+</mo>
             <msup>
               <mi>b</mi>
               <mn>2</mn>
             </msup>
           </mtd>
           <mtd>
             <mo>=</mo>
           </mtd>
           <mtd>
             <msup>
               <mi>c</mi>
               <mn>2</mn>
             </msup>
             <mo>+</mo>
             <mn>2</mn>
             <mi>a</mi>
             <mi>b</mi>
           </mtd>
         </mtr>
         <mtr>
           <mtd>
             <msup>
               <mi>a</mi>
               <mn>2</mn>
             </msup>
             <mo>+</mo>
             <msup>
               <mi>b</mi>
               <mn>2</mn>
             </msup>
           </mtd>
           <mtd>
             <mo>=</mo>
           </mtd>
           <mtd>
             <msup>
               <mi>c</mi>
               <mn>2</mn>
             </msup>
           </mtd>
         </mtr>
       </mtable>
     """),

    ("x = "
     "<mfrac>"
     "<mrow>-b±<msqrt><msup>b 2</msup>-4ac</msqrt></mrow>"
     "2a"
     "</mfrac>",

     """
       <mi>x</mi><mo>=</mo>
       <mfrac>
         <mrow>
           <mo>-</mo><mi>b</mi>
           <mo>±</mo>
           <msqrt>
             <msup><mi>b</mi><mn>2</mn></msup>
             <mrow>
               <mo>-</mo>
               <mn>4</mn>
               <mi>a</mi>
               <mi>c</mi>
             </mrow>
           </msqrt>
         </mrow>
         <mrow>
           <mn>2</mn>
           <mi>a</mi>
         </mrow>
       </mfrac>
     """),
]

for terse, verbose in test_cases:
    total += 1
    result = mathml_verbosifier.verbosify(terse)

    verbose = "".join(line.strip() for line in verbose.split("\n"))
    
    if verbose != result:
        failures += 1
        print("failure")
        print("  verbosify(%r)" % terse)
        print("  expected: %r" % verbose)
        print("       got: %r" % result)
        print()

if failures == 0:
    print("PASS")
else:
    print("FAIL: %s/%s" % (failures, total))
