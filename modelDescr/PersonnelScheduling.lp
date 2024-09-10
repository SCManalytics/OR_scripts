\* Workforce_planning_Problem *\
Minimize
Total_Cost_of_workers_per_shift: 112 Shift_FT12PM8PM + 112 Shift_FT4PM12AM
 + 112 Shift_FT8AM4PM + 48 Shift_PT12PM4PM + 48 Shift_PT4PM8PM
 + 48 Shift_PT8AM12PM + 48 Shift_PT8PM12AM
Subject To
firstShiftFtPtReq: Shift_FT8AM4PM - 2 Shift_PT8AM12PM >= 0
firstShiftReq: Shift_FT8AM4PM + Shift_PT8AM12PM >= 6
fourthShiftFtPtReq: Shift_FT4PM12AM - 2 Shift_PT8PM12AM >= 0
fourthShiftReq: Shift_FT4PM12AM + Shift_PT8PM12AM >= 6
secondShiftFtPtReq: Shift_FT12PM8PM + Shift_FT8AM4PM - 2 Shift_PT12PM4PM >= 0
secondShiftReq: Shift_FT12PM8PM + Shift_FT8AM4PM + Shift_PT12PM4PM >= 8
thirdShiftFtPtReq: Shift_FT12PM8PM + Shift_FT4PM12AM - 2 Shift_PT4PM8PM >= 0
thirdShiftReq: Shift_FT12PM8PM + Shift_FT4PM12AM + Shift_PT4PM8PM >= 12
End
