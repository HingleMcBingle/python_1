#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
#Convert the extracted value to a floating point number and print it out.

#data to extract from
text = "X-DSPAM-Confidence:    0.8475"

#variable to find 0 in text string
snumb = text.find("0")

#variable to find 5 in text string
enumb = text.find("5", snumb)

#variable for string inbewteen index location of snumb and enumb
fnumb = text[snumb:enumb+1]

print(float(fnumb))