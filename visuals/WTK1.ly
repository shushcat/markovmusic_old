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
    r8   g16[ c']   e'[ g c' e'] r8   g16[ c']   e'[ g c' e']   }
}

left = {
  \clef "bass"

  << {
    %% 0
    r16 e'8. ~ e'4 r16 e'8. ~ e'4 |
      } \\ {
    %% 0
    c'2 c' |
    } >>
  
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


