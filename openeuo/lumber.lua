-- utils
function has_value (tab, val)
    for index, value in ipairs(tab) do
        if value == val then
            return true
        end
    end

    return false
end

function checkJournal(jIndex,jLines)
  jIndex = jIndex or 0
  jLines = jLines or {}
  if type(jLines) ~= 'table' then jLines = {jLines} end
      	        	         
  local jTable = {}
  local bMatch = false
      	        	          
  local jI, jCnt = UO.ScanJournal(jIndex)
  if jCnt > 99 then
    jI, jCnt = UO.ScanJournal(jIndex)
  end
      	        	          
  for i = 0, jCnt - 1 do
    local jLine,jCol = UO.GetJournal(i)
    for _,v in pairs(jLines) do
      if jLine:match(v) then 
        bMatch = true
        table.insert(jTable,1,{Match = v, Line = jLine, Col = jCol})
      end
    end
  end
      	        	          
  return jI, bMatch, jTable
end

function findItem(targets, by, ignoreids)
 local nCnt = UO.ScanItems(true)
 
 if type(ignoreids) ~= 'table' then
  ignoreids = {}
 end
 
 if by == nil then
  by = 'type'
 end
 
 if type(targets) ~= 'table' then
  targets = {targets}
 end
 
 for i = 0, nCnt-1 do
  local found = {}
  found['id'], found['type'], found['kind'], found['contId'], found['x'], found['y'], found['z'], found['stack'], found['rep'], found['col'] = UO.GetItem(i)

  if not has_value(ignoreids, found['id']) then
   if has_value(targets, found[by]) then
    return found
   end
  end
 end
 return nil
end

function moveTo(i)
 UO.Move(i['x'], i['y'], 1, 10000)
 return f
end

-- ==========================================
-- services
-- ==========================================

TREE_TYPES = {
 3277,
 3280, 3286, 3288,
 3290, 3293, 3296, 3299,
 3500, 3501
}
AXE_TYPES = {3907, 3913}
                 
RUNE_BANK = 1159382571 
RUNE_TREE = 1159382570
CONT_LOG = 1129116001
LOG_TYPES = {7127, 12127, 12687, 12688, 12689}
IGNORE_TREES = {}
TREE = nil
AXE = nil
JOURNAL_IDX = 0

function initJournal()
 print('init journal')
 JOURNAL_IDX = checkJournal()
end

function moveToStart()
 UO.Move(683, 827, 1, 10000)
end

function equipAxe()
 if AXE then
  local equipped = findItem(AXE['id'], 'id')
  if equipped then
   return
  end
 end
 print('equip a axe')
 AXE = findItem(AXE_TYPES)
 UO.LObjectID = AXE['id']
 UO.Macro(17, 0)  
 wait(1000) 
end

function moveTree()
 print('move to tree')
 local f = findItem(TREE_TYPES, 'type', IGNORE_TREES)
 UO.Move(f['x'], f['y'], 1, 10000)
 TREE = f
end

function castRecall(id) 
 UO.Macro(15, 31)
 wait(2000)
 UO.LTargetID = id
 UO.Macro(22, 0)
end


function checkWeight()
 if UO.MaxWeight - UO.Weight > 20 then
  return
 end
 print('check weight')
 castRecall(RUNE_BANK)
 UO.Macro(1, 0, 'bank')
 while true do
  local log = findItem(LOG_TYPES, 'type')
  if not log then
   break
  end
  UO.Drag(log['id'], log['stack'])
  wait(100)
  UO.DropC(CONT_LOG)
  wait(1000)
 end
 castRecall(RUNE_TREE)
 wait(2000)
end

function chopTree()
 print('chop the tree')
 while true do
  if not findItem(TREE['id'], 'id') then
   break
  end
  equipAxe()
  UO.LObjectID = AXE['id']
  UO.Macro(17, 0) 
  wait (1000)    
  UO.LTargetID = TREE['id']    
  wait (1000)  
  UO.Macro(22, 0)
  wait (1000)
  
  -- check skill
  JOURNAL_IDX, isLackSkill, _ = checkJournal(JOURNAL_IDX, 'You lack the skill')
  if isLackSkill then
   print('lack skill')
   table.insert(IGNORE_TREES, TREE['id'])
   break
  end
 end
end


-- ==========================================
-- main
-- ==========================================
initJournal()
-- moveToStart()

while true do
 checkWeight()
 moveTree()   
 chopTree()
end