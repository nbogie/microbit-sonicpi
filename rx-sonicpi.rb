live_loop :playosc do
  use_real_time
  x,y,syn = sync "/osc/mbit/neill"
  n = choose([62, 64, 66, 69, 71, 74])
  use_synth syn
  play n,amp: 1, cutoff: y
  sleep 0.1
end

