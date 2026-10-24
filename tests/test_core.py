import unittest
from download_counter_episodes import run
class Tests(unittest.TestCase):
 def row(self,day,count,asset='a'):return {'asset':asset,'at':f'2026-10-{day:02d}T00:00:00Z','count':count}
 def test_baseline_excluded_and_monotone_delta(self):
  r=run({'snapshots':[self.row(1,100),self.row(2,103),self.row(3,108)]})['assets'][0];self.assertEqual(r['sum_observed_nondecreasing_deltas'],8);self.assertEqual(r['baseline_count'],100)
 def test_decrease_is_unknown_not_zero_or_new_downloads(self):
  r=run({'snapshots':[self.row(1,100),self.row(2,5),self.row(3,8)]})['assets'][0];self.assertIsNone(r['complete_increment_total_under_no_hidden_reset_or_correction']);self.assertIsNone(r['intervals'][0]['increase_under_no_reset_assumption']);self.assertEqual(r['sum_observed_nondecreasing_deltas'],3)
 def test_replacement_asset_not_subtracted_from_predecessor(self):self.assertTrue(all(not a['intervals']for a in run({'snapshots':[self.row(1,100),self.row(2,2,'b')]})['assets']))
 def test_out_of_order_snapshots_are_sorted_but_conflicts_rejected(self):
  self.assertEqual(run({'snapshots':[self.row(2,5),self.row(1,3)]})['assets'][0]['sum_observed_nondecreasing_deltas'],2)
  with self.assertRaises(ValueError):run({'snapshots':[self.row(1,3),self.row(1,4)]})
