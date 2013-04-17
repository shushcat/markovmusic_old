\version "2.14.2"

\header
{
title = "Das Wohltemperierte Klavier"
subtitle = "Preludium 1"
composer = "Johann Sebastian Bach"
}

\pointAndClickOff

%% 
%% Define the left and the right hand in new variables
%%
right = {
  \transpose c c' {
    \time 4/4
    \clef "violin"
    \tempo 4=60
    \set Score.tempoHideNote = ##t
    r8   g16[ c']   e'[ g c' e'] r8   g16[ c']   e'[ g c' e'] |\noBreak
    r8   a16[ d']   f'[ a d' f'] r8   a16[ d']   f'[ a d' f'] |\noBreak
    r8   g16[ d']   f'[ g d' f'] r8   g16[ d']   f'[ g d' f'] |
      }
}

left = {
  \clef "bass"

  << {
    %% 0
    r16 e'8. ~ e'4 r16 e'8. ~ e'4 |
    r16 d'8. ~ d'4 r16 d'8. ~ d'4 |
    r16 d'8. ~ d'4 r16 d'8. ~ d'4 |
   
  } \\ {
    %% 0
    c'2 c' |
    c' c' |
    b b |
     } >>
  
}

%%
%% Bring the two hands together
%%   
\score {
  \context PianoStaff <<
    \set PianoStaff.connectArpeggios = ##t
    \context Staff = "upper" \right
    \context Staff = "lower" \left
  >>
   \layout { }
   \midi { }
}



