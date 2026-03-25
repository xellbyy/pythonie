let input = req.query.input;
eval(input); // Noncompliant
(Function(input))(); // Noncompliant
eval(input); // Noncompliant
(new Function(input))(); // Noncompliant
