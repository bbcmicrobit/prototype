# Person module!
OPT MODULE

EXPORT ENUM NAME=1, PHONE, ADDRESS
EXPORT ENUM READ, WRITE
ENUM NOORDER, ORDER

EXPORT OBJECT person:
 PRIVATE:
   flat
   name, telephone
   address::PTR TO LONG
   telephone
 ENDATTRS
ENDOBJECT

EXPORT PROC mk(name,streetline1,streetline2,streetline3, city,county,postcode,telephone) OF person :
   self.flat:=NEW [name,streetline1,streetline2,streetline3,city,county,postcode,telephone]
   self.name:=name
   self.address:=NEW [streetline1,streetline2,streetline3,city,county,postcode]
   self.telephone:=telephone
ENDPROC

EXPORT PROC end() OF person:
   DEF f,a
   f:=self.flat
   a:=self.address
   END f[8], a[6] # Let's be polite shall we?
ENDPROC

EXPORT PROC name(mode=>READ, data=>NIL) OF person :
   IF (mode==READ):
      RETURN self.name
   ELSE:
      self.name:=data
   ENDIF
ENDPROC

EXPORT PROC telephone(mode=>READ, data=>NIL) OF person:
   IF (mode==READ):
      RETURN self.telephone
   ELSE:
      self.telephone:=data
   ENDIF
ENDPROC

EXPORT PROC address(mode=>READ, data=>NIL) OF person:
   # The format of this field would be private. It would be available so that
   #  given two individuals 'john' and 'fred' you could see if they lived at the
   #
   IF (mode==READ):
      RETURN self.address
   ELSE:
      NOP # No, you can't write something you don't know the format of...
   ENDIF
ENDPROC

EXPORT PROC flat() OF person IS self.flat
#      format is an array with data filled in in the same order as the parameters
#      to person.mk().
#      ie person.flat() <=> [name,streetline1,streetline2,streetline3,
#                            city,county,postcode,telephone]
#      evaluates to TRUE!

EXPORT PROC compare(field::PTR TO person,type=>NIL) OF person:
   DEF result=FALSE
   IF type:
      SELECT type:
         CASE NAME:
            result:=compare_name(self.name,field)
         CASE PHONE:
            result:=compare_telephone(self.telephone,field)
         CASE ADDRESS:
            result:=compare_address(self.address,field)
         CASE ALL:
            result:= TRUE AND compare_name(self.name,field.name()) AND compare_telephone(self.telephone,field.telephone()) AND compare_address(self.address,field.address())
         ENDCASES
      ENDSELECT
   ELSE:
      result:=compare_name(self.name,field,ORDER) # if type = NIL, ordering involved
   ENDIF
ENDPROC result

PROC compare_name(name1, name2, ordering=>NOORDER):
   DEF result=FALSE
   IF (ordering==NOORDER):
      # This branch enables the procedure to return
      # true if the name2 exists in name1
      result:= ((InStr name1,name2) <> -1) OR ((StrLen name2)==0)
   ELSE:
      NOP 
      # If we could introduce ordering, we could use a tree
      #     structure to speed up access times if there were
      #     *alot* of names and addresses
   ENDIF
ENDPROC result

PROC compare_telephone(tel1, tel2) IS ((InStr tel1,tel2)<>-1) OR ((StrLen tel2)==0)
#       Looks to see if the telephone number (fragment?)
#       tel2 passed exists inside tel1

PROC compare_address(address1::PTR TO LONG, address2::PTR TO LONG):
   #    Returns *TRUE* if the address2 exists _inside address1
   DEF result=TRUE, f
   FOR f:=0 TO 5:
      IF address2[f]:
         IF Not(((StrLen address2[f])==0) AND ((StrLen address1[f])==0)):
           #        The following line incorrectly(?) says that a
           #        NULL string does not exist inside a NULL string.
           #        The IF above corrects this 
           result:=result AND ( ((InStr address1[f],address2[f])<>-1) OR ((StrLen address2[f])==0) )
         ENDIF
      ENDIF
   ENDFOR
ENDPROC result

