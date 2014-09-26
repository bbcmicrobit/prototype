for fields in using query:
   SELECT first_name, last_name, table_contact.phone, e_mail, table_site.name :
     FROM table_contact, table_site
     WHERE table_contact.objid = "<CASECONTACTID>"
     AND table_site.objid = "<CASESITEID>"
   ENDSELECT
endfor
