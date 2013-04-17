\version "2.16.0"

\pointAndClickOff

%% 
%% Define the left and the right hand in new variables
%%
right = {
  \transpose c c' {
    \time 4/4
    \clef "treble"
    \tempo 4=60
    \set Score.tempoHideNote = ##t
    <  g c'   e' >1^"C Major"   }
}

left = {
  \clef "bass"

  << {<
    %% 0
     e' 
      >1} \\ {<
    %% 0
    c' 
    >1} >>
  
}

%%
%% Bring the two hands together
%%   
\score {
  \context PianoStaff <<
%%    \set PianoStaff.connectArpeggios = ##t
	
    \context Staff = "upper" \right
    \context Staff = "lower" \left
  >>
   \layout { }
 
}




