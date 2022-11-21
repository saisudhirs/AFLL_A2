# Quick Start
Run the m2.py file using:
 ```shell
python ./m2.py
 ```
Enter in **one line** of valid typescript if conditional statements.

The script will print `Valid String` if the string is valid.
Else, the script will print out the invalid token.

# Valid Strings
The script accepts most valid typescript (and consequently valid javascript) if conditionals.
Some notable ommisions include:
    - C style conditionals with no Curly Braces
    - Variable definitions within the if statement's expressions
    - Support for semicolon based delimitation

Another limitation is that it accepts only **one** line of input at a time.
This means that the complexity is limited.

Some strings you can use include
```typescript
if (x) {}
```

```typescript
if (x < 0) {}
```

```typescript
if (1 || 0) {}
```

```typescript
if (x[0]) {}
```
```typescript
if (x.y) {}
```

```typescript
if ((x.y && y[z]) || 10) {}
```
```typescript
if (x) {} else {}
```

```typescript
if (x) {if (2) {} } else {if (1) {} }
```
