# ItemPickerDiscordBot
A bot that takes in a list outputs a winner showing you an elimination process

uses 2 commands at the moment:
!wheel
!reroll

The wheel command lets you input a list of items for example: !wheel item1,item2, item 3, item 4 
these are seperated by commas and the wheel will output the following:
!wheel 1,2,3

1 has been eliminated...
:emote:Wheel:2, 3]
3 has been eliminated...
:emote:Wheel:2]
The Final winner is:2!
type !reroll to reroll the list again

The reroll command keeps a memory of the last list you used the wheel command on and automatically rerolls the previous list of items if you would like a different final outcome and follows the same format as above.

The sample.env should contain your own discord api key
