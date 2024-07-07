Title: Assumption Driven Development
date: 2014-09-29 20:00:00
slug: assumption-driven-development

Assumption driven development is when you develop based on assumption.
While this might sound weird, I believe this practice happens almost every
where.

There are two kinds of assumption driven development. The first one is
when some parts of the requirements aren't clear, and you, don't want to
spend more time back and forth asking questions, decide to make an
assumption on how stuff should work and move on with it. Sometimes you're
right, sometimes you're wrong. Not a big deal. As long as you're under the
deadline you're fine.

The other one is not writing tests for your code and assume it's working
because the documentation says so. This is a big no-no. No body writes
perfect code. Not even you. I'm always a big fan of tests. No comment 
in the code? no problem at all. Shipping code without tests? There's a
chance that I'll rewrite the code and write the test my own. Most likely
because I don't understand the code.

[Code without tests is broken as designed &mdash;Jacob Kaplan-Moss][brokencode].

[brokencode]: http://jacobian.org/writing/django-apps-with-buildout/#create-a-test-wrapper

