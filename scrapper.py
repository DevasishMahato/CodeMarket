from validate_email import validate_email

if __name__ == "__main__":
    email_list = ['t7.devasishmahato@gmail.com', 'devasishmahato@notexist.wim','t7.devasishmahato@codemarket.com','14.325@213.242','t7.devasish@cse.iiitp.ac.in']

    for em in email_list:
      if validate_email(em):
        print('correct email--->' + em)