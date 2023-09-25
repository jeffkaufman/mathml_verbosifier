# MathML Verbosifier

As specified, MathML is extremely verbose, and doesn't follow the early 90s
sprit of HTML as something you might want to hand-code. This script allows you
to write MathML as it should be, a terser version, and then losslessly convert
to MathML as understood by browsers.

There are only two changes from standardized MathML:

* Bare numbers, letters, and symbols are allowed, and are automatically assumed
  to be `<mn>`, `<mi>`, and `<mo>` respectively.

* A series of bare characters in a row, without whitespace, is automatically
  wrapped in an `<mrow>`.

For example, the quadratic formula in standard MathML could look like:

    <math>
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
    </math>

But we can write it less verbosely as:

    <math>
      x =
      <mfrac>
        <mrow>
          -b±
          <msqrt>
            <msup>b 2</msup>
            -4ac
          </msqrt>
        </mrow>
        2a
      </mfrac>
    </math>

Or, equivalently but with a bit less whitespace,

    <math>
      x =
      <mfrac>
        <mrow>-b±<msqrt><msup>b 2</msup>-4ac</msqrt></mrow>
        2a
      </mfrac>
    </math>

Example usage:

    import mathml_verbosify
    mathml_verbosify.verbosify(
      "<msup>a 2</msup> + <msup>b 2</msup> = <msup>c 2</msup>")

This is currently a proof-of-concept: good enough for my usage, but likely
missing important logic. The next step in turning this into something
production-ready would be to de-verbosify a the standard MathML test sets
([Mozilla](https://fred-wang.github.io/MathFonts/mozilla_mathml_test/),
[Wikipedia](http://eyeasme.com/Joe/MathML/MathML_browser_test.html)) and verify
that the verbosified versions render similarly.
