import ProjectSection from "@/components/ProjectCard";
export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center bg-[#050a05] text-white p-6 md:p-24 selection:bg-racing-light selection:text-white">
      
      {/* --- SECTION HERO (BIO) --- */}
      <section className="flex flex-col items-center text-center mb-24 animate-in fade-in slide-in-from-bottom-8 duration-1000">
        
        {/* Badge Formation Actuelle */}
        <div className="mb-8 px-4 py-1 border border-racing-light/40 rounded-full bg-racing-dark/20 backdrop-blur-sm">
          <span className="text-racing-light text-[10px] md:text-xs font-mono uppercase tracking-[0.2em]">
            Bachelor 2 Informatique & Numérique • ECE Bordeaux
          </span>
        </div>
        
        {/* Nom & Titre */}
        <h1 className="text-5xl md:text-8xl font-black tracking-tighter mb-6 leading-none">
          MATHIS <br className="md:hidden" />
          <span className="text-racing-light drop-shadow-[0_0_15px_rgba(34,197,94,0.3)]">LADINE CALOC</span>
        </h1>
        
        {/* Phrase d'accroche (Bio) */}
        <p className="max-w-2xl text-gray-400 text-base md:text-lg leading-relaxed font-light">
          Futur alternant en <span className="text-white font-medium">Bachelor 3 Data & IA</span>. 
          Passionné par l'ingénierie de la donnée et l'optimisation des systèmes, 
          avec un objectif clair : fusionner <span className="text-white font-medium">Data Science</span> et <span className="text-white font-medium">Haute Performance</span>.
        </p>
        
        {/* Badges Compétences Transverses (Aéro & Langues) */}
        <div className="mt-10 flex flex-wrap justify-center gap-4 text-[10px] font-mono">
          <div className="flex items-center gap-2 px-3 py-1.5 border border-white/10 rounded-md bg-white/[0.02]">
            <span className="w-2 h-2 rounded-full bg-blue-500 animate-pulse"></span>
            BREVET D'INITIATION AÉRONAUTIQUE (BIA)
          </div>
          <div className="flex items-center gap-2 px-3 py-1.5 border border-white/10 rounded-md bg-white/[0.02]">
            <span className="w-2 h-2 rounded-full bg-racing-light"></span>
            ANGLAIS : NIVEAU B2
          </div>
        </div>

        {/* Bouton Scroll/Action (Décoratif pour le style) */}
        <div className="mt-16 flex flex-col items-center gap-2 text-gray-600">
          <span className="text-[10px] uppercase tracking-widest font-mono">Découvrir mes projets</span>
          <div className="w-px h-12 bg-gradient-to-b from-racing-light to-transparent"></div>
        </div>
      </section>

      {/* --- SECTION PROJETS (APPEL DU COMPOSANT) --- */}
      <ProjectSection />
      
      {/* --- FOOTER CONTACT --- */}
      <footer className="mt-32 py-16 border-t border-white/5 w-full flex flex-col items-center gap-6">
        <div className="flex flex-wrap justify-center gap-8 text-sm text-gray-400 font-mono">
          <a href="mailto:theomat04@gmail.com" className="hover:text-racing-light transition-colors">theomat04@gmail.com</a>
          <span>07.83.36.08.69</span>
          <a href="#" className="hover:text-racing-light transition-colors underline decoration-racing-light/30 underline-offset-4">LinkedIn</a>
        </div>
        <p className="text-[10px] text-gray-600 uppercase tracking-widest">
          © 2026 • Codé avec Next.js & Passion pour la Data
        </p>
      </footer>

    </main>
  );
}