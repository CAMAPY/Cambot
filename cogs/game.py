import discord
import sys
from discord.ext import commands
from pretty_help import PrettyHelp,DefaultMenu
import random
from math import *
import os


class game(commands.Cog, description = "game?!"):

    def __init__(self,client): 
        self.client = client
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'game has been turned on {self.client.user}')
        
    @commands.command()
    async def wordle(self, ctx,difficulty):
        async def gameplay():
                win = False
                for i in range(int(difficulty)):
                    statement = (await self.client.wait_for('message', check = check)).content.lower()
                    answer = ''
                    print(word)
                    if statement != word:
                        for j in range(len(statement)):
                            if statement[j] in word:
                                if statement[j] in word[j]:
                                    k = '🟩'
                                else:
                                    k = '🟨'
                            else:
                                k = '❌'
                            answer += k
                        await ctx.send(answer)
                        await ctx.send(f"You've {int(difficulty) - i -1} more tries")
                    else:
                        win = True
                        await ctx.send("Congrats you won! ggwp")
                        break
                if win == False:
                    await cwin(win)
        async def replay():
                await ctx.send("Do you want to continue? (y/n)")
                choice = (await self.client.wait_for('message', check = check1)).content.lower()
                if choice == 'y':
                    await ctx.send("Alright, continue guessing!")
                    await gameplay()
                elif choice == 'n':
                    await ctx.send("lol nub, get gud")
                    return
                else:
                    await ctx.send("y/n, its a simple answer, retard. Stop wasting my time")
                    return
        async def cwin(win):
                    await ctx.send("Oops, Your out of tries, try again")
                    await replay()
        def check(message):
            return message.channel == ctx.channel and len(message.content) ==  int(difficulty)
        def check1(message):
            return message.channel == ctx.channel and message.author == ctx.author
        await ctx.send("Get ready to rack your brains for epic wordle game!")
        wordseasy = ['abs', 'add', 'bag', 'bad', 'cap', 'can', 'cam', 'cad', 'dad', 'dal', 'ear', 'eat', 'eco', 'fam', 'far', 'fan', 'gag', 'had', 'ham', 'ice', 'icy', 'jar', 'jam', 'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use']
        wordshard = ['abacus', 'baboon', 'babies', 'babble', 'cabbed', 'canned', 'cabbie', 'dabber', 'eager', 'eagles', 'fabled', 'fabric', 'facade', 'fables', 'gabble', 'habits', 'hacked', 'hackerkebabs', 'machos', 'pacify', 'pacing', 'pacers', 'packed', 'rabbit', 'tables', 'tabbed', 'tablas', 'udders', 'vacuum', 'vacant', 'vacate', 'wackos', 'yachts', 'zaatar', 'Better', 'Beyond', 'Bishop', 'Border', 'Bottle', 'Bottom', 'Bought', 'Branch', 'Breath', 'Bridge', 'Bright', 'Broken', 'Budget', 'Burden', 'Bureau', 'Button', 'Camera', 'Cancer', 'Cannot', 'Carbon', 'Career', 'Castle', 'Casual', 'Caught', 'Center', 'Centre', 'Chance', 'Change', 'Charge', 'Choice', 'Choose', 'Chosen', 'Church', 'Circle', 'Client', 'Closed', 'Closer', 'Coffee', 'Column', 'Combat', 'Coming', 'Common', 'Comply', 'Copper', 'Corner', 'Costly', 'County', 'Couple', 'Course', 'Covers', 'Create', 'Credit', 'Crisis', 'Custom', 'Damage', 'Danger', 'Dealer', 'Debate', 'Decade', 'Decide', 'Defeat', 'Defend', 'Define', 'Degree', 'Demand', 'Depend', 'Deputy', 'Desert', 'Design', 'Desire', 'Detail', 'Detect', 'Device', 'Differ', 'Dinner', 'Direct', 'Doctor', 'Dollar', 'Domain', 'Double', 'Driven', 'Driver', 'During', 'Easily', 'Eating', 'Editor', 'Effect', 'Effort', 'Eighth', 'Either', 'Eleven', 'Emerge', 'Empire', 'Employ', 'Enable', 'Ending', 'Energy', 'Engage', 'Engine', 'Enough', 'Ensure', 'Entire', 'Entity', 'Equity', 'Escape', 'Estate', 'Ethnic', 'Exceed', 'Except', 'Excess', 'Expand', 'Expect', 'Expert', 'Export', 'Extend', 'Extent', 'Fabric', 'Facing', 'Factor', 'Failed', 'Fairly', 'Fallen', 'Family', 'Famous', 'Father', 'Fellow', 'Female', 'Figure', 'Filing', 'Finger', 'Finish', 'Fiscal', 'Flight', 'Flying', 'Follow', 'Forced', 'Forest', 'Forget', 'Formal', 'Format', 'Former', 'Foster', 'Fought', 'Fourth', 'French', 'Friend', 'Future', 'Garden', 'Gather', 'Gender', 'German', 'Global', 'Golden', 'Ground', 'Growth', 'Guilty', 'Handed', 'Handle', 'Happen', 'Hardly', 'Headed', 'Health', 'Height', 'Hidden', 'Holder', 'Honest', 'Impact', 'Import', 'Income', 'Indeed', 'Injury', 'Inside', 'Intend', 'Intent', 'Invest', 'Island', 'Itself', 'Jersey', 'Joseph', 'Junior', 'Killed', 'Labour', 'Latest', 'Latter', 'Launch', 'Lawyer', 'Leader', 'League', 'Leaves', 'Legacy', 'Length', 'Lesson', 'Letter', 'Lights', 'Likely', 'Linked', 'Liquid', 'Listen', 'Little', 'Living', 'Losing', 'Lucent', 'Luxury', 'Mainly', 'Making', 'Manage', 'Manner', 'Manual', 'Margin', 'Marine', 'Marked', 'Market', 'Martin', 'Master', 'Matter', 'Mature', 'Medium', 'Member', 'Memory', 'Mental', 'Merely', 'Merger', 'Method', 'Middle', 'Miller', 'Mining', 'Minute', 'Mirror', 'Mobile', 'Modern', 'Modest', 'Module', 'Moment', 'Morris', 'Mostly', 'Mother', 'Motion', 'Moving', 'Murder', 'Museum', 'Mutual', 'Myself', 'Narrow', 'Nation', 'Native', 'Nature', 'Nearby', 'Nearly', 'Nights', 'Nobody', 'Normal', 'Notice', 'Notion', 'Number', 'Object', 'Obtain', 'Office', 'Offset', 'Online', 'Option', 'Orange', 'Origin', 'Output', 'Oxford', 'Packed', 'Palace', 'Parent', 'Partly', 'Patent', 'People', 'Period', 'Permit', 'Person', 'Phrase', 'Picked', 'Planet', 'Player', 'Please', 'Plenty', 'Pocket', 'Police', 'Policy', 'Prefer', 'Pretty', 'Prince', 'Prison', 'Profit', 'Proper', 'Proven', 'Public', 'Pursue', 'Raised', 'Random', 'Rarely', 'Rather', 'Rating', 'Reader', 'Really', 'Reason', 'Recall', 'Recent', 'Record', 'Reduce', 'Reform', 'Regard', 'Regime', 'Region', 'Relate', 'Relief', 'Remain', 'Remote', 'Remove', 'Repair', 'Repeat', 'Replay', 'Report', 'Rescue', 'Resort', 'Result', 'Retail', 'Retain', 'Return', 'Reveal', 'Review', 'Reward', 'Riding', 'Rising', 'Robust', 'Ruling', 'Safety', 'Salary', 'Sample', 'Saving', 'Saying', 'Scheme', 'School', 'Screen', 'Search', 'Season', 'Second', 'Secret', 'Sector', 'Secure', 'Seeing', 'Select', 'Seller', 'Senior', 'Series', 'Server', 'Settle', 'Severe', 'Sexual', 'Should', 'Signal', 'Signed', 'Silent', 'Silver', 'Simple', 'Simply', 'Single', 'Sister', 'Slight', 'Smooth', 'Social', 'Solely', 'Sought', 'Source', 'Soviet', 'Speech', 'Spirit', 'Spoken', 'Spread', 'Spring', 'Square', 'Stable', 'Status', 'Steady', 'Stolen', 'Strain', 'Stream', 'Street', 'Stress', 'Strict', 'Strike', 'String', 'Strong', 'Struck', 'Studio', 'Submit', 'Sudden', 'Suffer', 'Summer', 'Summit', 'Supply', 'Surely', 'Survey', 'Switch', 'Symbol', 'System', 'Taking', 'Talent', 'Target', 'Taught', 'Tenant', 'Tender', 'Tennis', 'Thanks', 'Theory', 'Thirty', 'Though', 'Threat', 'Thrown', 'Ticket', 'Timely', 'Timing', 'Tissue', 'Toward', 'Travel', 'Treaty', 'Trying', 'Twelve', 'Twenty', 'Unable', 'Unique', 'United', 'Unless', 'Unlike', 'Update', 'Useful', 'Valley', 'Varied', 'Vendor', 'Versus', 'Victim', 'Vision', 'Visual', 'Volume', 'Walker', 'Wealth', 'Weekly', 'Weight', 'Wholly', 'Window', 'Winner', 'Winter', 'Within', 'Wonder', 'Worker', 'Wright', 'Writer', 'Yellow']
        win = False
        if difficulty == '3':
            word = random.choice(wordseasy).lower()
            await ctx.send(f'Start guessing a {difficulty} lettered word')
            win = False 
            await gameplay()
            await ctx.send(f"The answer was {word}")
        elif difficulty == "6":
            word = random.choice(wordshard).lower()
            await ctx.send(f'Start guessing a {difficulty} lettered word')
            await gameplay()
            await ctx.send(f"The answer was {word}")
        else:
            await ctx.send("But maybe choose either 6 or 3 as a length cos my owner is lazy :)")


def setup(client):
    client.add_cog(game(client))