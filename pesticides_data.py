# Detailed Pesticides and Prevention Data for Plant Diseases
# This data covers all 39 label categories used in the classification model.

PESTICIDES_DATA = {
    'Apple___Apple_scab': {
        'pesticides': [
            'Captan (Standard chemical fungicide)',
            'Mancozeb (Dithane M-45)',
            'Myclobutanil (Immunox)',
            'Copper soap / Liquid Copper Fungicide (Organic alternative)'
        ],
        'prevention': 'Prune apple tree branches to improve airflow, rake and destroy all fallen leaves in autumn, and apply organic mulch to prevent fungal spores from splashing up from the soil.'
    },
    'Apple___Black_rot': {
        'pesticides': [
            'Captan',
            'Thiophanate-methyl (Cleary 3336)',
            'Copper-based fungicides',
            'Sulfur sprays (Organic preventative)'
        ],
        'prevention': 'Prune out dead wood and cankers during winter dormancy. Remove and destroy any mummified fruit remaining on the trees or the ground.'
    },
    'Apple___Cedar_apple_rust': {
        'pesticides': [
            'Myclobutanil (Immunox)',
            'Mancozeb (Dithane)',
            'Copper fungicides (Apply at bud break)',
            'Sulfur (Organic preventative)'
        ],
        'prevention': 'Remove nearby Eastern Red Cedar or other juniper hosts (within 1-2 miles if possible). Plant rust-resistant apple cultivars.'
    },
    'Apple___healthy': {
        'pesticides': [],
        'prevention': 'Prune annually to maintain structure and airflow, apply high-quality compost, mulch the base, and monitor weekly for pests.'
    },
    'Background_without_leaves': {
        'pesticides': [],
        'prevention': 'To get a correct prediction, please upload a clear, well-lit close-up image focusing on a single leaf of the target plant.'
    },
    'Blueberry___healthy': {
        'pesticides': [],
        'prevention': 'Ensure soil pH is kept acidic (4.5 to 5.5). Mulch with pine bark, water deeply (1-2 inches per week), and prune in late winter.'
    },
    'Cherry___Powdery_mildew': {
        'pesticides': [
            'Potassium bicarbonate (MilStop)',
            'Neem Oil (Organic horticultural spray)',
            'Myclobutanil (Immunox)',
            'Wettable Sulfur'
        ],
        'prevention': 'Prune cherry trees to open up the canopy and allow sunlight penetration and wind drying. Avoid overhead watering.'
    },
    'Cherry___healthy': {
        'pesticides': [],
        'prevention': 'Apply balanced fertilizer in early spring, paint lower trunks with white latex paint to avoid winter sunscald, and maintain proper drainage.'
    },
    'Corn___Cercospora_leaf_spot Gray_leaf_spot': {
        'pesticides': [
            'Propiconazole (Tilt)',
            'Pyraclostrobin (Headline)',
            'Azoxystrobin (Quadris)'
        ],
        'prevention': 'Practice crop rotation with non-grass crops (such as soybeans). Till corn residue into the soil to accelerate decomposition of fungal hosts.'
    },
    'Corn___Common_rust': {
        'pesticides': [
            'Pyraclostrobin (Headline)',
            'Azoxystrobin (Quadris)',
            'Mancozeb'
        ],
        'prevention': 'Select rust-resistant corn hybrids. Avoid overhead sprinkler irrigation if rust is active, and clear grassy weeds from borders.'
    },
    'Corn___Northern_Leaf_Blight': {
        'pesticides': [
            'Propiconazole (Tilt)',
            'Azoxystrobin (Quadris)',
            'Pyraclostrobin (Headline)',
            'Mancozeb'
        ],
        'prevention': 'Plant resistant hybrids, rotate crops to break the disease cycle, and manage crop residue. Avoid excess nitrogen fertilization.'
    },
    'Corn___healthy': {
        'pesticides': [],
        'prevention': 'Perform crop rotations, monitor fields for pests, maintain correct planting density to manage moisture, and optimize fertilizer application.'
    },
    'Grape___Black_rot': {
        'pesticides': [
            'Mancozeb (Dithane)',
            'Captan',
            'Myclobutanil (Rally)',
            'Copper Hydroxide (Kocide)'
        ],
        'prevention': 'Ensure vines are trained on trellises off the ground. Prune out infected canes and remove all mummified berries from the vineyard.'
    },
    'Grape___Esca_(Black_Measles)': {
        'pesticides': [
            'Trichoderma harzianum (Biological bio-fungicide)',
            'Thiophanate-methyl wound protectants (applied directly to pruning wounds)'
        ],
        'prevention': 'Seal larger pruning wounds immediately to prevent spore entry. Avoid mechanical wounds to vine trunks, and prune only during dry periods.'
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'pesticides': [
            'Copper-based fungicides',
            'Mancozeb',
            'Captan'
        ],
        'prevention': 'Clean up and burn or bury fallen leaf litter in late autumn. Prune the grapevine canopy to allow sunlight and maximize air circulation.'
    },
    'Grape___healthy': {
        'pesticides': [],
        'prevention': 'Prune vines annually in late winter, keep weeds down around root zones, apply mulch, and keep shoots trained on trellis systems.'
    },
    'Orange___Haunglongbing_(Citrus_greening)': {
        'pesticides': [
            'Imidacloprid (Systemic insecticide to control Psyllid vectors)',
            'Thiamethoxam (Actara)',
            'Horticultural oils or Neem oil (organic vector control)'
        ],
        'prevention': 'Citrus greening has no chemical cure once infected. Strictly control the Asian Citrus Psyllid vector. Promptly remove and burn infected trees to save the grove.'
    },
    'Peach___Bacterial_spot': {
        'pesticides': [
            'Copper Hydroxide (Kocide - apply during dormant/early season)',
            'Oxytetracycline (Mycoshield / FireLine)',
            'Bacillus subtilis (Serenade ASO - bio-bactericide)'
        ],
        'prevention': 'Avoid planting highly susceptible peach cultivars. Manage nitrogen inputs to prevent rapid, tender foliage growth which is highly vulnerable.'
    },
    'Peach___healthy': {
        'pesticides': [],
        'prevention': 'Apply a dormant lime-sulfur spray in late winter to prevent leaf curl. Thin peaches in spring to prevent overcrowding and fruit rot.'
    },
    'Pepper,_bell___Bacterial_spot': {
        'pesticides': [
            'Copper hydroxide mixed with Mancozeb (synergistic mix)',
            'Streptomycin (Agri-Mycin)',
            'Bacillus subtilis (Serenade)'
        ],
        'prevention': 'Use certified disease-free seeds and seedlings. Rotate pepper plants with non-solanaceous crops (e.g. corn, beans). Do not touch wet plants.'
    },
    'Pepper,_bell___healthy': {
        'pesticides': [],
        'prevention': 'Mulch to preserve soil moisture, install stakes/cages to keep fruit off the ground, water at the soil level, and keep weeds under control.'
    },
    'Potato___Early_blight': {
        'pesticides': [
            'Chlorothalonil (Daconil)',
            'Mancozeb',
            'Azoxystrobin',
            'Copper soap (Organic)'
        ],
        'prevention': 'Rotate potato crops with non-solanaceous crops every 2-3 years. Ensure the soil has balanced potassium. Mulch to keep lower leaves dry.'
    },
    'Potato___Late_blight': {
        'pesticides': [
            'Chlorothalonil',
            'Mancozeb',
            'Cymoxanil (Curzate)',
            'Copper Hydroxide (Kocide)'
        ],
        'prevention': 'Destroy volunteer potato plants and wild nightshades. Use certified disease-free seed tubers. Avoid overhead irrigation to limit wetness.'
    },
    'Potato___healthy': {
        'pesticides': [],
        'prevention': 'Hill up soil around the growing potato tubers to protect them from spores, rotate crops, and monitor for Colorado Potato Beetles.'
    },
    'Raspberry___healthy': {
        'pesticides': [],
        'prevention': 'Prune out old, fruited floricanes in winter. Space plants to ensure dry leaves, provide trellising, and mulch around roots.'
    },
    'Soybean___healthy': {
        'pesticides': [],
        'prevention': 'Practice crop rotations with corn, plant high-vigor treated seeds, manage weeds, and inspect for soybean aphids.'
    },
    'Squash___Powdery_mildew': {
        'pesticides': [
            'Potassium bicarbonate (GreenCure)',
            'Neem Oil (Organic preventative)',
            'Sulfur dust or spray',
            'Myclobutanil'
        ],
        'prevention': 'Space squash plants widely. Direct water to the soil base rather than overhead. Plant squash in open areas with maximum sunshine.'
    },
    'Strawberry___Leaf_scorch': {
        'pesticides': [
            'Captan',
            'Copper-based fungicides',
            'Thiophanate-methyl'
        ],
        'prevention': 'Renovate strawberry beds after harvest by mowing leaves. Plant in well-drained soil and avoid low-lying wet spots.'
    },
    'Strawberry___healthy': {
        'pesticides': [],
        'prevention': 'Mulch beds with clean straw to keep berries off damp ground. Clean up old runners, and plant new beds every 3-4 years.'
    },
    'Tomato___Bacterial_spot': {
        'pesticides': [
            'Copper Hydroxide combined with Mancozeb',
            'Streptomycin (Agri-Mycin)',
            'Serenade (Bacillus subtilis - organic bactericide)'
        ],
        'prevention': 'Rotate crops annually. Disinfect stakes, cages, and pruning tools with a 10% bleach solution. Avoid working in wet fields.'
    },
    'Tomato___Early_blight': {
        'pesticides': [
            'Chlorothalonil (Daconil)',
            'Mancozeb (Dithane)',
            'Copper fungicide (Organic)'
        ],
        'prevention': 'Prune the lowest 12 inches of leaves to prevent soil splash onto foliage. Apply thick mulch, and water at the base using drip irrigation.'
    },
    'Tomato___Late_blight': {
        'pesticides': [
            'Chlorothalonil',
            'Mancozeb',
            'Copper-based fungicides',
            'Metalaxyl-M (Ridomil Gold)'
        ],
        'prevention': 'Immediately pull up, bag, and discard infected plants (do not compost). Plant blight-resistant tomato cultivars, and avoid overhead watering.'
    },
    'Tomato___Leaf_Mold': {
        'pesticides': [
            'Chlorothalonil',
            'Copper fungicide',
            'Mancozeb'
        ],
        'prevention': 'Keep relative humidity below 85% in greenhouses. Prune suckers and crowded leaves to improve ventilation. Keep leaves dry.'
    },
    'Tomato___Septoria_leaf_spot': {
        'pesticides': [
            'Chlorothalonil (Daconil)',
            'Mancozeb (Dithane)',
            'Copper Hydroxide'
        ],
        'prevention': 'Practice a 3-year crop rotation (no tomatoes, peppers, potatoes, or eggplants). Mulch the ground and clean up crop residue in autumn.'
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'pesticides': [
            'Abamectin (Agri-Mek)',
            'Spiromesifen (Oberon)',
            'Insecticidal soap (Organic contact spray)',
            'Neem Oil (Organic)'
        ],
        'prevention': 'Regularly spray the undersides of leaves with a strong stream of water to dislodge mites. Keep plants well-hydrated to reduce mite attraction.'
    },
    'Tomato___Target_Spot': {
        'pesticides': [
            'Chlorothalonil',
            'Copper-based fungicides',
            'Azoxystrobin'
        ],
        'prevention': 'Avoid planting tomatoes close together. Prune lower suckers to maximize airflow. Clean stakes and tomato cages thoroughly after harvest.'
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'pesticides': [
            'Imidacloprid (Systemic insecticide to control Whiteflies)',
            'Acetamiprid',
            'Neem oil / Insecticidal soaps (Organic vector control)'
        ],
        'prevention': 'The virus is spread by Silverleaf Whiteflies. Protect seedlings with fine insect netting, hang yellow sticky cards, and remove infected plants immediately.'
    },
    'Tomato___Tomato_mosaic_virus': {
        'pesticides': [
            'Trisodium Phosphate (TSP - used for sterilizing garden tools)',
            'Reconstituted Non-Fat Dry Milk (spray on leaves; proteins help deactivate virus on contact)'
        ],
        'prevention': 'No chemical cure. Extremely contagious; spreads by touch. Wash hands with soap and disinfect tools before handling plants. Avoid smoking near tomatoes.'
    },
    'Tomato___healthy': {
        'pesticides': [],
        'prevention': 'Maintain consistent soil moisture to prevent blossom end rot, mulch roots, feed with tomato-specific fertilizer, and prune suckers.'
    }
}
