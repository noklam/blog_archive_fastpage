class Solution:
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        def is_overnight(startTime, finishTime):
            if startTime > finishTime:
                return True
            else:
                return False
            
        def str_to_HHMM(time):
            HH, MM = time[:2], time[3:]
            print("Before", HH, MM)

            if HH[0] == "0":
                HH = HH[1]
            if MM[0] == "0":
                MM = MM[1]
            print("After", HH, MM)
            return int(HH), int(MM)
        
        startHH, startMM = str_to_HHMM(startTime)
        finishHH, finishMM = str_to_HHMM(finishTime)
        
        # Convert Hour to Minute
        start_elapse = startHH * 60 + startMM
        finish_elapse = finishHH * 60 + finishMM
        
        if is_overnight(start_elapse, finish_elapse):
            finish_elapse += 60* 24
        
        # Main Logic
        # round start and finish time to the closest end time
        start_elapse = math.ceil(start_elapse / 15) * 15
        finish_elapse = math.floor(finish_elapse / 15) * 15
        
        full_minutes = finish_elapse - start_elapse
        return full_minutes // 15
            
            