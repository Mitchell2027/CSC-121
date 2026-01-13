# Created a program to analyze and clean customer feedback with different string methods.(Functions.py)
# 24 November 2025
# CSC121 M6Pro
# Mariah Mitchell

import re

def clean_name(name):
    '''
    Clean and format a customer's name.
    
    Parameters
    ----------
    name : str
        The raw name input.

    Returns
    -------
    str
        Cleaned, title-cased name

    '''
    #Removes trailing spaces
    #Capitalize first letter of each word
    return name.strip().title()


def clean_email(email):
    '''
    Clean and standarized an email address.

    Parameters
    ----------
    email : str
        The raw email input.

    Returns
    -------
    str
        Cleaned, lowercase email.

    '''
    #Removes extra spaces
    #Converts all letter to lowercase
    return email.strip().lower()


def clean_product(product):
    '''
    Clean and format a product name.
    
    Parameters
    ----------
    product : str
        The raw product input.

    Returns
    -------
    str
        Cleaned, title-cased product name.

    '''
    #Removes trailing spaces
    #Capitalize first letter of each word
    return product.strip().title()


def clean_feedback(feedback):
    '''
    Clean and format customer feedback text.
    
    Parameters
    ----------
    feedback : str
        The raw feedback input.

    Returns
    -------
    text : str
        Cleaned feedback text.

    '''
    #Removes Spaces
    #Capitalize the first letter
    #Replace repeated punctuation
    #Replace multiple space with a single space
    text = feedback.strip()
    text = text.capitalize()
    text = re.sub(r"[!?.]{2,}", lambda m: m.group()[0], text)
    text = re.sub(r"\s{2,}", " ", text)
    return text


def is_valid_name(name):
    '''
    Validate a customer's name.
    
    Parameters
    ----------
    name : str
       The name to validate

    Returns
    -------
    bool
        True if valid, False otherwise.

    '''
    #Valdidate that name contains only letter and spaces
    return all(part.isalpha() for part in name.replace(" ", ""))


def is_valid_email(email):
    '''
    Validate email address

    Parameters
    ----------
    email : str
        The email to validate.

    Returns
    -------
    bool
        True if valid, False otherwise.

    '''
    #Checks email validation
    #Prevents invalid emails
    return ("@" in email) and (email.endswith(".com") or email.endswith(".net"))


def contains_negative(feedback):
    '''
    Check if feedback contains negative words.
    
    Parameters
    ----------
    feedback : str
        The feedback to analyze.

    Returns
    -------
    bool
        True if any negative words are found, False otherwise.

    '''
    #Checks feedback for negative words
    negative_words = ["poor", "broke", "so-so"]
    lowered = feedback.lower()
    return any(word in lowered for word in negative_words)


def write_entry(file, name, email, product, feedback):
    '''
    Write a formatted feedback entry to a text file.
    
    Parameters
    ----------
    file : file object
        The open file to write to.
    name : str
        Customer's name.
    email : str
        Customer's email.
    product : str
        Product name.
    feedback : str
        Feedback text.

    Returns
    -------
    None.

    '''
    #Write a formatted feedback entry to a file.
    file.write(f"Name: {name}\n")
    file.write(f"Email: {email}\n")
    file.write(f"Product: {product}\n")
    file.write(f"Feedback: {feedback}\n")
    file.write("-----------------------------\n")