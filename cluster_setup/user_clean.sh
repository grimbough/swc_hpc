
#!/bin/bash
## clean all user directories

n=40
for i in `seq -w 1 ${n}`
do
  echo $i;

  sudo rm /home/user${i}/embl_swc_hpc
  sudo rm /home/user${i}/.bash_history

done
