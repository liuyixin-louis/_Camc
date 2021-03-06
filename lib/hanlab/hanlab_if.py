
from .agent import DDPG, train
import logging


msglogger = logging.getLogger()


class ArgsContainer(object):
    def __init__(self):
        pass


class RlLibInterface(object):
    """Interface to a hanlab DDPG impelementation."""

    def solve(self, env, args):
        msglogger.info("CACP: Using hanlab")
        
        agent_args = ArgsContainer()
        agent_args.bsize = args.batch_size
        agent_args.tau = 0.01
        agent_args.discount = 1.
        agent_args.epsilon = 50000
        agent_args.init_delta = 0.5
        agent_args.delta_decay = 0.95
        agent_args.warmup = env.cacp_cfg.ddpg_cfg.num_heatup_episodes
        agent_args.lr_c = env.cacp_cfg.ddpg_cfg.critic_lr
        agent_args.lr_a = env.cacp_cfg.ddpg_cfg.actor_lr
        agent_args.hidden1 = 300
        agent_args.hidden2 = 300
        agent_args.rmsize = env.cacp_cfg.ddpg_cfg.replay_buffer_size
        agent_args.window_length = 1
        agent_args.train_episode = (env.cacp_cfg.ddpg_cfg.num_heatup_episodes +
                                    env.cacp_cfg.ddpg_cfg.num_training_episodes)
        agent_args.output = "."
        agent_args.conditional = args.conditional
        agent = DDPG(args.observation_len, 1, agent_args)
        train(agent_args.train_episode, agent, env, agent_args.output, agent_args.warmup)

