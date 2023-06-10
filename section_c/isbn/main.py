def isbn13(isbn):

    def _is_valid_isbn13(isbn):
        sum_product_isbn13 = sum(int(digit) * (1 if i % 2 == 0 else 3) for i, digit in enumerate(isbn))
        if sum_product_isbn13 % 10 == 0:
            return "Valid"
        else:
            return "Invalid"
    
    if (len(isbn) == 13) and isbn.isdigit() and isbn[-1] != 'X':
       return _is_valid_isbn13(isbn)
  
    if len(isbn) == 10:
        if isbn[:-1].isdigit() and (isbn[-1].isdigit() or isbn[-1] == 'X'):
            # Verify checksum
            total = sum(int(digit) * (10 - i) for i, digit in enumerate(isbn[:-1]))
            if isbn[-1] == 'X':
                total += 10
            else:
                total += int(isbn[-1])
            
            if total % 11 == 0:
                # Convert to ISBN-13
                isbn13 = "978" + isbn[:-1]
                converted_total = sum(int(digit) * (1 if i % 2 == 0 else 3) for i, digit in enumerate(isbn13))
                check_digit = (10 - (converted_total % 10)) % 10
                isbn13 += str(check_digit)
                return isbn13
            else:
                return "Invalid"
        else:
            return "Invalid"
    
    
if __name__ == "__main__":
    print(isbn13("0330301824")) # Invalid
    print(isbn13("877195869X")) # 9788771958690
    print(isbn13("9780316066525")) # Valid
    print(isbn13("0316066524")) # 9780316066525


