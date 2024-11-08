political_index = {
    'Alabama': {
        'presidential_voting': {  # 30 points max
            'dem_votes': 849624,
            'rep_votes': 1441170,
            'total_votes': 2323282,
            'winner_margin': ((1441170 - 849624) / 2323282) * 100,  # 25.5% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {  # 40 points max
            'control': 'R',
            'chamber_control': 20,  # Full R control
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {  # 30 points max
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Republican leaning
    },
      'Arizona': {
        'presidential_voting': {
            'dem_votes': 1672143,
            'rep_votes': 1661686,
            'total_votes': 3387326,
            'winner_margin': ((1672143 - 1661686) / 3387326) * 100,  # 0.3% D margin
            'winner': 'D',
            'points': 3  # Low points for very close margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 7,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 7,
            'length_control': 3
        },
        'total_index': 65  # Moderate Republican leaning
      },
    'Arkansas': {
    'presidential_voting': {  # 30 points max
        'dem_votes': 423932,
        'rep_votes': 760647,
        'total_votes': 1219069,
        'winner_margin': ((760647 - 423932) / 1219069) * 100,  # 27.6% R margin
        'winner': 'R',
        'points': 15  # Full points for >15% margin
    },
    'legislature_control': {  # 40 points max
        'control': 'R',
        'chamber_control': 20,  # Full R control
        'margin_control': 10,   # Strong majority
        'length_control': 10    # Long-term control
    },
    'governor': {  # 30 points max
        'party': 'R',
        'points': 15,
        'margin_victory': 10,
        'length_control': 5
    },
    'total_index': 85  # Strong Republican leaning
    },
    'California': {
        'presidential_voting': {
            'dem_votes': 11110639,
            'rep_votes': 6006518,
            'total_votes': 17501380,
            'winner_margin': ((11110639 - 6006518) / 17501380) * 100,  # 29.2% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Democratic leaning
    },
    'Colorado': {
        'presidential_voting': {
            'dem_votes': 1804352,
            'rep_votes': 1364607,
            'total_votes': 3256980,
            'winner_margin': ((1804352 - 1364607) / 3256980) * 100,  # 13.5% D margin
            'winner': 'D',
            'points': 12  # Points for 10-15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 8,    # Moderate majority
            'length_control': 8     # Recent but stable control
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 7,
            'length_control': 3
        },
        'total_index': 73  # Moderate Democratic leaning
    },
    'Connecticut': {
        'presidential_voting': {  # 30 points max
            'dem_votes': 1080831,
            'rep_votes': 714717,
            'total_votes': 1823857,
            'winner_margin': ((1080831 - 714717) / 1823857) * 100,  # 20.1% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {  # 40 points max
            'control': 'D',
            'chamber_control': 20,  # Full D control
            'margin_control': 8,    # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {  # 30 points max
            'party': 'D',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 80  # Strong Democratic leaning
    },
    'Delaware': {
        'presidential_voting': {
            'dem_votes': 296268,
            'rep_votes': 200603,
            'total_votes': 504346,
            'winner_margin': ((296268 - 200603) / 504346) * 100,  # 19% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 8,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 80  # Strong Democratic leaning
    },
    'Florida': {
        'presidential_voting': {
            'dem_votes': 5297045,
            'rep_votes': 5668731,
            'total_votes': 11067456,
            'winner_margin': ((5668731 - 5297045) / 11067456) * 100,  # 3.4% R margin
            'winner': 'R',
            'points': 5  # Low points for close margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,   # Strong majority (84-36 in House)
            'length_control': 10    # Long-term control
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 7,
            'length_control': 4
        },
        'total_index': 71  # Strong Republican leaning
    },
    'Georgia': {
        'presidential_voting': {  # 30 points max
            'dem_votes': 2473633,
            'rep_votes': 2461854,
            'total_votes': 4999960,
            'winner_margin': ((2473633 - 2461854) / 4999960) * 100,  # 0.2% D margin
            'winner': 'D',
            'points': 3  # Low points for very close margin
        },
        'legislature_control': {  # 40 points max
            'control': 'R',
            'chamber_control': 20,  # Full R control
            'margin_control': 8,    # Moderate majority
            'length_control': 10    # Long-term control
        },
        'governor': {  # 30 points max
            'party': 'R',
            'points': 15,
            'margin_victory': 7,
            'length_control': 4
        },
        'total_index': 67  # Moderate Republican leaning
    },
    'Hawaii': {
        'presidential_voting': {
            'dem_votes': 366130,
            'rep_votes': 196864,
            'total_votes': 574469,
            'winner_margin': ((366130 - 196864) / 574469) * 100,  # 29.5% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Democratic leaning
    },
    'Idaho': {
        'presidential_voting': {
            'dem_votes': 287021,
            'rep_votes': 554119,
            'total_votes': 867934,
            'winner_margin': ((554119 - 287021) / 867934) * 100,  # 30.8% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Republican leaning
    },
    'Illinois': {
        'presidential_voting': {  # 30 points max
            'dem_votes': 3471915,
            'rep_votes': 2446891,
            'total_votes': 6033744,
            'winner_margin': ((3471915 - 2446891) / 6033744) * 100,  # 17% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {  # 40 points max
            'control': 'D',
            'chamber_control': 20,  # Full D control
            'margin_control': 9,    # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {  # 30 points max
            'party': 'D',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 81  # Strong Democratic leaning
    },
    'Indiana': {
        'presidential_voting': {
            'dem_votes': 1242498,
            'rep_votes': 1729857,
            'total_votes': 3033210,
            'winner_margin': ((1729857 - 1242498) / 3033210) * 100,  # 16.1% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 8,
            'length_control': 5
        },
        'total_index': 83  # Strong Republican leaning
    },
    'Iowa': {
        'presidential_voting': {
            'dem_votes': 759061,
            'rep_votes': 897672,
            'total_votes': 1690871,
            'winner_margin': ((897672 - 759061) / 1690871) * 100,  # 8.2% R margin
            'winner': 'R',
            'points': 8  # Points for 5-10% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 8,
            'length_control': 8
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 7,
            'length_control': 4
        },
        'total_index': 70  # Moderate Republican leaning
    },
    'Kansas': {
        'presidential_voting': {
            'dem_votes': 570323,
            'rep_votes': 771406,
            'total_votes': 1373986,
            'winner_margin': ((771406 - 570323) / 1373986) * 100,  # 14.6% R margin
            'winner': 'R',
            'points': 12  # Points for 10-15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 9,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 5,
            'length_control': 3
        },
        'total_index': 74  # Moderate Republican leaning
    },
    'Kentucky': {
        'presidential_voting': {
            'dem_votes': 772474,
            'rep_votes': 1326646,
            'total_votes': 2136768,
            'winner_margin': ((1326646 - 772474) / 2136768) * 100,  # 25.9% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 5,
            'length_control': 2
        },
        'total_index': 77  # Strong Republican leaning
    },
      'Louisiana': {
        'presidential_voting': {  # 30 points max
            'dem_votes': 856034,
            'rep_votes': 1255776,
            'total_votes': 2148062,
            'winner_margin': ((1255776 - 856034) / 2148062) * 100,  # 18.6% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {  # 40 points max
            'control': 'R',
            'chamber_control': 20,  # Full R control
            'margin_control': 10,   # Strong majority (68-35 House, 27-12 Senate)
            'length_control': 10    # Long-term control
        },
        'governor': {  # 30 points max
            'party': 'D',
            'points': 15,
            'margin_victory': 7,
            'length_control': 3
        },
        'total_index': 80  # Strong Republican leaning
    },
    'Maine': {
        'presidential_voting': {
            'dem_votes': 435072,
            'rep_votes': 360737,
            'total_votes': 819461,
            'winner_margin': ((435072 - 360737) / 819461) * 100,  # 9.1% D margin
            'winner': 'D',
            'points': 8  # Points for 5-10% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,  # D control (21-14 Senate, 89-57 House)
            'margin_control': 8,
            'length_control': 8
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 71  # Moderate Democratic leaning
    },
    'Maryland': {
        'presidential_voting': {
            'dem_votes': 1985023,
            'rep_votes': 976414,
            'total_votes': 3037030,
            'winner_margin': ((1985023 - 976414) / 3037030) * 100,  # 33.2% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,  # D supermajority (32-15 Senate, 99-42 House)
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 7,
            'length_control': 4
        },
        'total_index': 81  # Strong Democratic leaning
    },
    'Massachusetts': {
        'presidential_voting': {
            'dem_votes': 2382202,
            'rep_votes': 1167202,
            'total_votes': 3631402,
            'winner_margin': ((2382202 - 1167202) / 3631402) * 100,  # 33.5% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 10,   # Strong D majority
            'length_control': 10    # Long-term control
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 82  # Strong Democratic leaning
    },
    'Michigan': {
        'presidential_voting': {
            'dem_votes': 2804040,
            'rep_votes': 2649852,
            'total_votes': 5539302,
            'winner_margin': ((2804040 - 2649852) / 5539302) * 100,  # 2.8% D margin
            'winner': 'D',
            'points': 3  # Low points for close margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 8,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 5,
            'length_control': 3
        },
        'total_index': 64  # Competitive/Moderate leaning
    },
      'Minnesota': {
        'presidential_voting': {  # 30 points max
            'dem_votes': 1717077,
            'rep_votes': 1484065,
            'total_votes': 3277171,
            'winner_margin': ((1717077 - 1484065) / 3277171) * 100,  # 7.1% D margin
            'winner': 'D',
            'points': 7  # Points for 5-10% margin
        },
        'legislature_control': {  # 40 points max
            'control': 'Split',
            'chamber_control': 10,  # Split control
            'margin_control': 5,    # Narrow margins
            'length_control': 5     # Recent split
        },
        'governor': {  # 30 points max
            'party': 'D',
            'points': 15,
            'margin_victory': 7,
            'length_control': 4
        },
        'total_index': 53  # Competitive/Moderate Democratic leaning
    },
    'Mississippi': {
        'presidential_voting': {
            'dem_votes': 539398,
            'rep_votes': 756764,
            'total_votes': 1313759,
            'winner_margin': ((756764 - 539398) / 1313759) * 100,  # 16.5% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Republican leaning
    },
    'Missouri': {
        'presidential_voting': {
            'dem_votes': 1253014,
            'rep_votes': 1718736,
            'total_votes': 3025962,
            'winner_margin': ((1718736 - 1253014) / 3025962) * 100,  # 15.4% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 8,
            'length_control': 5
        },
        'total_index': 83  # Strong Republican leaning
    },
    'Montana': {
        'presidential_voting': {
            'dem_votes': 244786,
            'rep_votes': 343602,
            'total_votes': 603674,
            'winner_margin': ((343602 - 244786) / 603674) * 100,  # 16.4% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 8,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 7,
            'length_control': 3
        },
        'total_index': 78  # Strong Republican leaning
    },
    'Nebraska': {
        'presidential_voting': {
            'dem_votes': 374583,
            'rep_votes': 556846,
            'total_votes': 956383,
            'winner_margin': ((556846 - 374583) / 956383) * 100,  # 19.1% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,  # Technically nonpartisan but Republican-majority
            'margin_control': 8,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 83  # Strong Republican leaning
    },
    'Nevada': {
        'presidential_voting': {
            'dem_votes': 703486,
            'rep_votes': 669890,
            'total_votes': 1405376,
            'winner_margin': ((703486 - 669890) / 1405376) * 100,  # 2.4% D margin
            'winner': 'D',
            'points': 3  # Low points for close margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 7,
            'length_control': 8
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 5,
            'length_control': 3
        },
        'total_index': 61  # Moderate Democratic leaning
    },
      'New Hampshire': {
        'presidential_voting': {  # 30 points max
            'dem_votes': 424937,
            'rep_votes': 365660,
            'total_votes': 806205,
            'winner_margin': ((424937 - 365660) / 806205) * 100,  # 7.4% D margin
            'winner': 'D',
            'points': 7  # Points for 5-10% margin
        },
        'legislature_control': {  # 40 points max
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 7,
            'length_control': 8
        },
        'governor': {  # 30 points max
            'party': 'R',
            'points': 15,
            'margin_victory': 7,
            'length_control': 4
        },
        'total_index': 68  # Moderate Republican leaning
    },
    'New Jersey': {
        'presidential_voting': {
            'dem_votes': 2608400,
            'rep_votes': 1883313,
            'total_votes': 4549457,
            'winner_margin': ((2608400 - 1883313) / 4549457) * 100,  # 15.9% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 82  # Strong Democratic leaning
    },
    'New Mexico': {
        'presidential_voting': {
            'dem_votes': 501614,
            'rep_votes': 401894,
            'total_votes': 923965,
            'winner_margin': ((501614 - 401894) / 923965) * 100,  # 10.8% D margin
            'winner': 'D',
            'points': 10  # Points for 10-15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 8,
            'length_control': 8
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 7,
            'length_control': 4
        },
        'total_index': 72  # Moderate Democratic leaning
    },
    'New York': {
        'presidential_voting': {
            'dem_votes': 5244886,
            'rep_votes': 3251997,
            'total_votes': 8616861,
            'winner_margin': ((5244886 - 3251997) / 8616861) * 100,  # 23.1% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Democratic leaning
    },
    'North Carolina': {
        'presidential_voting': {
            'dem_votes': 2684292,
            'rep_votes': 2758775,
            'total_votes': 5524804,
            'winner_margin': ((2758775 - 2684292) / 5524804) * 100,  # 1.3% R margin
            'winner': 'R',
            'points': 3  # Low points for close margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 8,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 5,
            'length_control': 3
        },
        'total_index': 64  # Competitive/Moderate leaning
    },
    'North Dakota': {
        'presidential_voting': {
            'dem_votes': 115042,
            'rep_votes': 235751,
            'total_votes': 362024,
            'winner_margin': ((235751 - 115042) / 362024) * 100,  # 33.3% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Republican leaning
    },
    'Ohio': {
        'presidential_voting': {  # 30 points max
            'dem_votes': 2679165,
            'rep_votes': 3154834,
            'total_votes': 5922202,
            'winner_margin': ((3154834 - 2679165) / 5922202) * 100,  # 8.03% R margin
            'winner': 'R',
            'points': 8  # Points for 5-10% margin
        },
        'legislature_control': {  # 40 points max
            'control': 'R',
            'chamber_control': 20,  # Full R control
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {  # 30 points max
            'party': 'R',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 75  # Strong Republican leaning
    },
    'Oklahoma': {
        'presidential_voting': {
            'dem_votes': 503890,
            'rep_votes': 1020280,
            'total_votes': 1560699,
            'winner_margin': ((1020280 - 503890) / 1560699) * 100,  # 33.1% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Republican leaning
    },
    'Oregon': {
        'presidential_voting': {
            'dem_votes': 1340383,
            'rep_votes': 958448,
            'total_votes': 2374321,
            'winner_margin': ((1340383 - 958448) / 2374321) * 100,  # 16.1% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 8,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 7,
            'length_control': 4
        },
        'total_index': 79  # Strong Democratic leaning
    },
    'Pennsylvania': {
        'presidential_voting': {
            'dem_votes': 3458229,
            'rep_votes': 3377674,
            'total_votes': 6936976,
            'winner_margin': ((3458229 - 3377674) / 6936976) * 100,  # 1.16% D margin
            'winner': 'D',
            'points': 3  # Low points for close margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 8,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 5,
            'length_control': 3
        },
        'total_index': 64  # Competitive/Moderate leaning
    },
    'Rhode Island': {
        'presidential_voting': {
            'dem_votes': 307486,
            'rep_votes': 199922,
            'total_votes': 517757,
            'winner_margin': ((307486 - 199922) / 517757) * 100,  # 20.8% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 82  # Strong Democratic leaning
    },
    'South Carolina': {
        'presidential_voting': {
            'dem_votes': 1091541,
            'rep_votes': 1385103,
            'total_votes': 2513329,
            'winner_margin': ((1385103 - 1091541) / 2513329) * 100,  # 11.7% R margin
            'winner': 'R',
            'points': 10  # Points for 10-15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 77  # Strong Republican leaning
    },
    'South Dakota': {
        'presidential_voting': {
            'dem_votes': 150471,
            'rep_votes': 261043,
            'total_votes': 422609,
            'winner_margin': ((261043 - 150471) / 422609) * 100,  # 26.2% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Republican leaning
    },
     'Tennessee': {
        'presidential_voting': {  # 30 points max
            'dem_votes': 1143711,
            'rep_votes': 1852475,
            'total_votes': 3053851,
            'winner_margin': ((1852475 - 1143711) / 3053851) * 100,  # 23.2% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {  # 40 points max
            'control': 'R',
            'chamber_control': 20,  # Full R control
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {  # 30 points max
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Republican leaning
    },
    'Texas': {
        'presidential_voting': {
            'dem_votes': 5259126,
            'rep_votes': 5890347,
            'total_votes': 11315056,
            'winner_margin': ((5890347 - 5259126) / 11315056) * 100,  # 5.6% R margin
            'winner': 'R',
            'points': 5  # Points for 5-10% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 9,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 71  # Strong Republican leaning
    },
    'Utah': {
        'presidential_voting': {
            'dem_votes': 560282,
            'rep_votes': 865140,
            'total_votes': 1488289,
            'winner_margin': ((865140 - 560282) / 1488289) * 100,  # 20.5% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Republican leaning
    },
    'Vermont': {
        'presidential_voting': {
            'dem_votes': 242820,
            'rep_votes': 112704,
            'total_votes': 367428,
            'winner_margin': ((242820 - 112704) / 367428) * 100,  # 35.4% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 10,
            'length_control': 10
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 8,
            'length_control': 4
        },
        'total_index': 82  # Strong Democratic leaning
    },
    'Virginia': {
        'presidential_voting': {
            'dem_votes': 2413568,
            'rep_votes': 1962430,
            'total_votes': 4460524,
            'winner_margin': ((2413568 - 1962430) / 4460524) * 100,  # 10.1% D margin
            'winner': 'D',
            'points': 10  # Points for 10-15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 8,
            'length_control': 6
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 7,
            'length_control': 4
        },
        'total_index': 70  # Moderate Democratic leaning
    },
    'Washington': {
        'presidential_voting': {
            'dem_votes': 2369612,
            'rep_votes': 1584651,
            'total_votes': 4087631,
            'winner_margin': ((2369612 - 1584651) / 4087631) * 100,  # 19.2% D margin
            'winner': 'D',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'D',
            'chamber_control': 20,
            'margin_control': 9,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 84  # Strong Democratic leaning
    },
    'West Virginia': {
        'presidential_voting': {  # 30 points max
            'dem_votes': 235984,
            'rep_votes': 545382,
            'total_votes': 794731,
            'winner_margin': ((545382 - 235984) / 794731) * 100,  # 38.9% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {  # 40 points max
            'control': 'R',
            'chamber_control': 20,  # Full R control
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {  # 30 points max
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Republican leaning
    },
    'Wisconsin': {
        'presidential_voting': {
            'dem_votes': 1630866,
            'rep_votes': 1610184,
            'total_votes': 3298041,
            'winner_margin': ((1630866 - 1610184) / 3298041) * 100,  # 0.6% D margin
            'winner': 'D',
            'points': 3  # Low points for very close margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 8,
            'length_control': 10
        },
        'governor': {
            'party': 'D',
            'points': 15,
            'margin_victory': 5,
            'length_control': 3
        },
        'total_index': 64  # Competitive/Moderate leaning
    },
    'Wyoming': {
        'presidential_voting': {
            'dem_votes': 73491,
            'rep_votes': 193559,
            'total_votes': 276765,
            'winner_margin': ((193559 - 73491) / 276765) * 100,  # 43.4% R margin
            'winner': 'R',
            'points': 15  # Full points for >15% margin
        },
        'legislature_control': {
            'control': 'R',
            'chamber_control': 20,
            'margin_control': 10,   # Strong majority
            'length_control': 10    # Long-term control
        },
        'governor': {
            'party': 'R',
            'points': 15,
            'margin_victory': 10,
            'length_control': 5
        },
        'total_index': 85  # Strong Republican leaning
    }
}

'''
Calculations and Data Cleaning
'''
