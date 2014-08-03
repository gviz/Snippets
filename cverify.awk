#Checks for c functions without proper closing braces.
#expects the function return type ,name and parameters on the same line
#usage awk -f <thisfile> <c source>
#/"main" ~ "^[:blank:]*[^\#]*[iuvc][:blank:]*.*\(.*\)[^\;]+"/

BEGIN{
    ob = 0
    cb = 0
    msg="Inspecting %s [Line: %d ] --- [ %s ]"
    succ="CLEAN"
    fail="Open Braces"
    first=1
    msgx=""
    ln=0
    infunc = 0
  }

/\{/{
#  print $0
#  print ob
    ob++
}

/\}/{
#print $0
#print ob
  if(ob > 0)
    ob--
   if(ob == 0) 
    infunc = 0
}

e23w323433[^\{\}\\\>\"]$/{
  if(length==0) next
  if($0 ~ /^[^\#]*[iuvc]+[ \t]*.*\(.*\)[^\;]*$/)
    next
   if($0 !~ /\;/){
    if($0 ~ /\)$/){
      if(infunc == 1) 
        next
    }
    msgx = sprintf(msg,fname,NR,"Missing SemiColumn [;]")
    print msgx
  }

}

#Function Definition
/^[^\#]*[iuvc]+[ \t]*.*\(.*\)[^\;]*$/ {
#  print $0 
#  print ob
  infunc = 1
  if(first == 1){
      first = 0
	    fname = $0
      ln = NR
      next 
    }
    if(ob != 0){
     msgx = sprintf(msg,fname,ln,fail)
    ob = 0

    print msgx 
  }else{
    msgx=sprintf(msg,fname,ln,succ)
    print msgx
  }
  ln = NR
  fname = $0
}

END{
  if(ob == 0){
      msgx = sprintf(msg,fname,ln,succ)
    }else{
      msgx = sprintf(msg,fname,ln,fail)
  }
  print msgx
}

 
