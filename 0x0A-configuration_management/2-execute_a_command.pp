# Define an exec resource to kill the process named "killmenow"

exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/bin'], 
  onlyif  => 'pgrep -f killmenow',
}
