#!/usr/bin/env ruby
# Requirement for Ruby Upload 02 about Meta-Programming
#
#
# a) Comments required: Add your Name
#    remove this comments or other unused lines of code
#
# b) Ruby-Specials:
#      create a method "on demand"
#    REQUIRED:
#      use of "method_missing" and "instance_eval"
#
# NOTE: ONLY ONE LINE of OUTPUT is allowed
#      Created,Inherited,2017 by FH JOANNEUM Kapfenberg,Done



class Snippet
#### START of my CODE ####

# add code for a class 'Snippet' with a
#    property "html"
# class Snippet can add new methods to it's class on demand
# expect methods names as follows: add_<tag>_tag
# e.g.: add_div_h2_tag("some text")
#       to add e.g. "<H2>some text</H2>" to its html-source

#### END of my CODE ####
end


# Do not mofify:
# calling a given code block
def run_now( &code_to_eval )
  puts code_to_eval.call() # <div>FHJ</div><div>ITM</div><h3>SWD</h3><h3>IMS</h3>
end

# call run <code block>
run_now {
  a = Snippet.new

  a.add_div_tag("FHJ")   # creates and add a method add_div_tag(...) to object a
  a.add_Div_tag("ITM")   # creates and add a method add_Div_tag(...) to object a
  # not required, but you could also support multiple args:
  #a.add_div_tag("SWD","IMS","IRM")

  a.add_h3_tag("SWD")    # creates and add a method add_h3_tag(...) to object a
  a.add_h3_tag("IMS")    # calls existing method add_h3_tag(...)

  a.html # return output of last statement
}
