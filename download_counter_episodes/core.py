import datetime as dt
from .common import integer,identifier

def run(data):
 rows=data['snapshots']
 if not isinstance(rows,list)or len(rows)>10000:raise ValueError('snapshots')
 groups={}
 for row in rows:
  asset=identifier(row['asset']);t=dt.datetime.fromisoformat(row['at'].replace('Z','+00:00'))
  if t.tzinfo is None:raise ValueError('aware_time')
  t=t.astimezone(dt.timezone.utc);count=integer(row['count'],0,10**15);groups.setdefault(asset,{})
  if t in groups[asset]and groups[asset][t]!=count:raise ValueError('contradictory_snapshot')
  groups[asset][t]=count
 outputs=[]
 for asset,values in sorted(groups.items()):
  ordered=sorted(values.items());intervals=[];known=0;unknown=0
  for(a,x),(b,y)in zip(ordered,ordered[1:]):
   decrease=y<x
   if decrease:unknown+=1
   else:known+=y-x
   intervals.append({'from':a.isoformat(),'to':b.isoformat(),'counter_delta':y-x,'increase_under_no_reset_assumption':None if decrease else y-x,'status':'counter_decreased_reset_or_correction_unknown'if decrease else'nondecreasing_observation'})
  outputs.append({'asset':asset,'baseline_count':ordered[0][1],'intervals':intervals,'sum_observed_nondecreasing_deltas':known,'unknown_decrease_intervals':unknown,'complete_increment_total_under_no_hidden_reset_or_correction':known if not unknown else None})
 return {'assets':outputs,'assumption':'counters_are_cumulative_without_unobserved_resets_or_corrections_between_nondecreasing_snapshots','model':'per_asset_counter_episode_receipts_initial_counts_not_new_downloads_no_human_identity'}
