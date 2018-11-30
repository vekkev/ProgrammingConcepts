 #live Coding Nov30th18

#! /usr/bin/env ruby
# Ruby "" 30. November 2018 14:00-17:00 ONL 1 https://meet.lync.com/fhjoanneum-edu/lynctest10/7ZCYRFYK
# execute this etherpad at your computer in the terminal using:
#  curl 'https://houston.fh-joanneum.at/ep_moodle/p/g.gTDJSRbfaSeq5HSx$moodle/export/txt' > /tmp/tst.rb 2>/dev/null; ruby /tmp/tst.rb

# puts "RUBY Metaprogramming participants: JFeiner, DReindl, MWalzl, LWechtitsch, ASchadler, MFeil, KSchmid, CRadlingmayer, BMaderer, LLeopold, KGruber, NOlah, HGschwend, MPrem, AKraus, ASowinska, ASackl, SSchoenegger, KKoch, DSpanner, AKlautzer, AWagner,JBaier, AFeichtinger,MGurdet,MLeitold, LHaidacher, MKlug, AKozlova, ASauer, FTrencehvski, NSucher, LLadinig, IGrasenick, PDürnberger, EKatic, PDvorak, CFressl, MTomberger, LSarcevic, NKaehling, ABektas"
# bitte wegen mir (walzl) und herrn reindl kurz chat checken
# Review Students A-Z
# gofunctions & channels
# see code GIT-IIT <https://git-iit.fh-joanneum.at/ProgKonz/2018ws-itm17-prog-konz>

#// EXTENSION
#// (1) defer// (2) recover from error
#// (3) closing channels
#// (4) split task and start many concurrent gofunctions
#// (5) wait for more than one channel at the same time#
# // (6) get value UNLESS proceed=false

# Meta-programming in Ruby
# GREAT RUBY ideas (e.g. RoR): DRY, CoC, Scaffolding, ....
# see slide a page 12: Philosophy by Matz Matsumoto (Japan)

# Quick Intro: Tools: irb, (ri, erb, ..)

# very special ruby: (read in english): puts,  do ... end, {... }, , empty?, ... call methods without ()
# very special: lambda, &block, proc, yield, ...
#  lambda {|x| 3x}
# Proc.new {}
# def m &block
#  block.call
# yield ... if block_given?
#
# very special: "wide open classes":
# @attribute, getter/setter: attr_accessor, constructor: initialise, to_s, ...
# OOP operator overloading: def <=>(other), ...
# modify = overwrite functionality / extend class with: "mixins", ..


  puts "Ruby simple examples"
  class Message
    def initialize m
      @msg=m
    end
    def to_s
      "Calling: #{ @msg }"
    end
    def method_missing (name, *args)
      puts "no idea how to handle #{name}"
# 'invent' a new method
      code = %Q(

def #{name}
puts "new method #{name} works."
end

)
      self.class.class_eval (code )
# self.send( meth_name, args) if self.respond_to? meth_name
    end
  end

  class SecureMessage < Message
    def initialize(m)
      super(m)
    end
  end

  class SecureMessage
    def secure_output
      puts("***")
    end
  end

  m = SecureMessage.new("Hello SWD")

  m.encrypt # <= method_missing: no idea how to handle encrypt
  m.encrypt # <= method_missing: ?

  puts m.secure_output

# Meta-programming in Ruby

# Inspection
# kind_of?, respond_to?, is_a?


# Monkey Patching (eval)
# alias methods
# instance_eval, class_eval

# Hooks (method missing?)
# at_exit do ... end
# calling "not-existing methods": method_missing? <= see Slides Rb01b page 12 5/5 Metaprogramming
#
  at_exit {
    puts "bye"
  }

# TODO code your class
#    with "toString, constructor,..."
# objekt erstellen
#   dynamisch zur laufzeit methode hinzufügen
#      method_missing
# z.B.:
# SongText
#     unbekannte Methode: find_words_start_with_b

# coffee & code until 15:55

# we need code to discuss =>
# name & code (wie weit Sie auch immer bei der Umsetzung gekommen sind)

# paste your work here:
#Lucca Ladinig:
  class SongFinder
    def initialize
    end

    def to_s
      return 'Nothing yet...'
    end

    def method_missing(name, *args)
      puts "no idea how to handle '#{name}'"
      puts "Trying to figure it out, though..."

      if name.to_s.include? 'find'

        code = %Q(
                                def #{name}(song)
                                        @song = song
                                end

                                def to_s
                                        return @song
                                end
                        )


        self.class.class_eval(code)

      else
        puts 'Nope, no idea...'
      end
    end
  end

  s = SongFinder.new
  puts s.to_s
  s.find_song('Lucy in the sky with diamonds')
  s.find_song('Lucy in the sky with diamonds')
  s.find_song('Hey bulldog!')
#funktioniert leider noch nicht...

# Bernd Maderer
  class Message
    def initialize(m)
      @msg=m
    end
    def to_s
      "Calling: #{ @msg }"
    end
    def method_missing (name, *args)
      puts "no idea how to handle #{name}"
      code = %Q(
def #{name}
 puts "new method #{name} works."
end
 )
      self.class.class_eval (code )
    end
  end

  msg = Message.new("Hello SWD")
  puts( "#{msg}")
  msg.find_words_start_with_b
  msg.find_words_start_with_b


#Lukas Wechtitsch
  class Buch
    def initialize(buchtitel, buchpreis)
      @titel=buchtitel
      @preis=buchpreis
    end

    def get_price
      "Das Buch kostet #{ @preis }"
    end

    def to_s
      "Titel des Buches: #{ @titel }"
    end

    def method_missing (name, *args)
      puts "Was bedeutet #{name}"
      # 'invent' a new method
      code = %Q(
    def #{name}
      buch1 = Buch.new("Extra Buch", 1);

      puts "#{args[0]} kauft sicher ein Buch"
    end
    )

      self.class.class_eval (code )
    end

    buch1 = Buch.new("Nettes Buch", 2);
    buch1.get_price
    buch1.irgendwas
  end





#Anastasiia Kozlova

  class SongText
    def initialize(name, singer, text)
      @songtext_name = name
      @songtext_singer = singer
      @songtext_text = text
    end

    def to_s
      "#{ @songtext_singer } '#{ @songtext_name }': #{ @songtext_text }"
    end

    def method_missing (name, *args)
      puts "method #{name} not found"
      code = %Q(

      def #{name}
      # hier möchte ich eine Liste mit all Methods erzeugen und in der Liste suchen, ob etwas passendes gibt
      # leider die Zeit war nicht genug
        puts "#{name} - Das kann ich leider nicht machen."
        puts "Ich singe dann lalalalalalala"
      end

    )
      self.class.class_eval (code )
    end
  end

  song = SongText.new("Weinachtslied", "Nikolaus", "Lalalala lalal lalalalala")

  song.find_words_start_with_b
  song.find_words_start_with_b

#Markus Tomberger
  class Car
    def initialize b
      @brand = b
    end
    def to_s
      "A car made by #{@brand}"
    end
    def method_missing (name, *args)
      puts "the car doesn't know how to #{name}"
      method = %Q(
      def #{name}
        puts "the car learned how to #{name}"
      end
    )
      self.class.class_eval (method)
    end
  end

  car = Car.new("an bankrupt company")
  puts "#{car}"
  puts ""
  car.drive
  car.drive
  puts ""
  car.crash
  car.crash
# ~ Online Mitarbeits-Abgabe


  class SongText

    def initialize text
      @text = text
    end

    def to_s
      @text
    end

    def method_missing name, *args
      matches = /find_words_starts_with_(.+)/.match name
      raise if matches.nil?

      self.class.class_eval %(
            def #{name}
                @text.split.select { |w| w.start_with? "#{matches[1]}" }
            end
        )
      self.send(name)
    end

  end

  def print_separator
    puts "*" * 40
  end

  song_text = SongText.new %Q(
Kommt drauf an wie du die Dinge siehst, die Dinge nimmst
Ganz egal wie tief du auch immer sinkst
Denk einfach wie ich dann handelst du die Sachen jetzt in Zukunft ganz bestimmt mit links

Du bist heute hier, morgen vielleicht weg
Hast bis jetzt geschlafen doch du wirst geweckt
Rumheulen hatte doch noch nie n Zweck
Auch der letzte Honk im Land kapiert das jetzt
)

  puts "Songtext"
  print song_text

  print_separator
  puts "Words starting with D"
  puts song_text.find_words_starts_with_D

  print_separator
  puts "Words starting with d"
  puts song_text.find_words_starts_with_d

  print_separator
  puts "Words starting with d (again)"
  puts song_text.find_words_starts_with_d

  print_separator
  puts "'die' occurrences"
  puts song_text.find_words_starts_with_die.length


# Klug Michael

  class Sample
    def initialize sampleText
      @sampleText = sampleText
    end
    def to_s
      "Sample Text: #{ @sampleText }"
    end
    def hello
      puts "Hello Ruby!"
    end
    def method_missing(m, *args)
      puts "There's no method called #{m}, call it again and it will work."
      code = %Q(
def #{name}
puts "new method #{name} works."
end
)
      self.class.class_eval (code )
    end
  end

  sample = Sample. new "I am Groot"
  puts sample
  sample.sepp
  sample.sepp

# Domain Specific Languages (DSL) <= see Slides Rb02 ProgConc DSL !!!
# internal vs. external DSL
# internal DSL: (but looks more like a configuration):
#  => code example "download", "statistics about the text/tags",  ...
# your work: extend: "save-to-file"
  https://houston.fh-joanneum.at/ep_moodle/p/g.4fJZB6P2G18cV1RI$moodle


# demo DSL
###########

  download "http://a.b.e/animals.html" do
    description "All the tags: "
    statistics :minlen => 4 do |tag|
      puts " Another important tag is '#{tag}'!"
    end
  end


  download "http://a.b.c/some.txt" do
    statistics :word => "dog"
    statistics :char => "v"
  end
  download "http://a.b.d/another.txt" do
    statistics :word => "dog"
  end
  download "http://a.b.d/animals.names" do
    save :txt => "animals.txt"
    statistics :word => "cat"
  end

  download "http://a.b.d/animals.names" do
    save :JSON => "animals.json"
    statistics :word => "cat"
  end

  download "http://a.b.e/animals.html" do
    description "All the tags: "
    statistics :minlen => 4 do |tag|
      puts " another tag '#{tag}' "
    end
  end