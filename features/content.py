general_doc = {
      "Introduction": 
        "The CellCognition object features!"
       }

group_doc = {
      "Basic shape features":
        r"Basic features are characterizing the shape of an object.",
      
      "Haralick features":
        r"The Haralick features that aim at characterizing the texture of objects by "
        r"means of joint distribution of pixel value combinations.",
        
      "Basic intensity features":
        r"Basic features characerize the intensity and its variation of an object.",
        
      "Convex hull features":
        r"The convex hull of a binary image is the smallest convex set "
        r"containing the image. Several object features can be derived from the convex hull "
        r"and from the set difference." ,
        
      "Distance map features":
        r"Distance map features are object features derived from the euclidean distance transform (distance map) "
        r"of the image",
        
      "Granulometry features":
        r"Granulomety features characterize the size distribution of objects (or "
        r"structures) in an image. For this, the image is successively "
        r"simplified by morphological operators.",
        
      "Moments":
        r"Moments and derived features have been are defined to "
        r"characterize distributions of pixel values (like histograms).",
        
      "Statistical geometric features":
        r"Statistical geometric features collect statistics of shape and texture measurements "
        r"applied to the binarized image at several thresholds levels",
      }

category_doc = {
    "circularity":
        r"Circularity features estimate of the <i>roundness</i> of the object",
    
    "convexhull":
        r"The convex hull $\mathrm{Conv}(X)$ of a set $X$ (binary image) is the smallest convex set containing $X$. Important features can "
        r"be derived from the convex hull and from the set difference $D = \mathrm{Conv}(X) \setminus X$. "
        "\n"
        r"To study the maximal areas of the connected components of $D$ is useful in order to find binuclear cell "
        r"nuclei for instance. A perfect binuclear cell should have two concavities of more or less the same "
        r"area. A trinuclear cell will have three concavities of similar size, if the three nuclei are positioned on "
        r"the corners of a triangle. If three nuclei are positioned in a row, the number of concavities is either higher "
        r"or the concavities have no symmetric size." 
        "\n"
        r"The size distribution of concavities is certainly a powerful feature. But we cannot conclude directly the "
        r"number of possibly involved cell nuclei. The reason is that a 'bended' row of several nuclei results on one "
        r"side in one large concavity and on the other side in several small concavities. In order to deal with this "
        r"problem, it would be good, to be able to control the degree or size of concavity we are interested in. This "
        r"can be done by the use of granulometries.",
    
    "distance-map-dynamics":
        r"Let $D_X$ be the "
        r"distance map of set $X$ (binary image), i.e. $D_X(x)$ is the distance "
        r"of pixel $x \in X$ to the nearest pixel $y \notin X$. If the object "
        r"corresponds to an ellipse, one can expect one prominent " 
        r"maximum in the distance function. If it could be decomposed into two "
        r"overlapping ellipses, where each of these ellipses are well "
        r"recognizable, on would expect two prominent maxima. Actually, if the "
        r"basic shapes are sufficiently prominent, the number of prominent "
        r"maxima should be the same as the number of the basic shapes.",
    
    "geometry":
        r"Geometry features describe basic geometric properties of an object.",
    
    "granulometry":
        r"Granulometry allows one to study the size distribution of objects (or"
        r"structures) in an image. For this, the image is successively simplified by operators which remove all (bright "
        r"or dark) structures up to a certain size. A record is kept of how much is removed from the image with each "
        r"filtering step, leading to a distribution of measurements $m_i$, which can be seen as size dependent texture "
        r"or shape descriptors. Each anti-extensive (extensive), increasing and "
        r"absorptive operator $\psi$ with $\psi_0 f = f$ can be used for the definition of a granulometry "
        r"<a class='ref_link' href='#ref-serra:83'>[3]</a>. These properties make sure that the family of operators behaves like a set of sieves with "
        r"increasing size. The sieves remove larger grains of the substance to be sieved. In practice, morphological "
        r"openings ($\gamma$: anti-extensive) and closings ($\phi$: extensive) are mostly used for this purpose. "
#        r"In figure \ref{fig:granulometry}, the successive application of closings with increasing size are shown in "
#        r"the first row: the concavities are successively filled. In the second row, the successive application of "
#        r"openings with increasing size is shown: small details are successively removed."
        "\n" 
        r"Let $\gamma_{sB}$ be a morphological opening with the structuring element $B$ of size $s$. Then the family " 
        r"$\Gamma = \{ \gamma_{sB}\}$ defines a series of operators which can be successively applied to the image $f$. " 
        r"For each step, we record a measure (e.g. the sum of gray level values) of what has been removed from the image. " 
        r"Hence, we obtain a list of measures $m_i = m(s_i)$ with $s_i \in \{s_1, s_2, s_3, \ldots \}$. We have used the "
        r"volume and the area, where the image volume $\mathrm{Vol}(\cdot)$ means the sum of gray levels and the area $\mathrm{Area}(\cdot)$" 
        r"means the number of non zero pixels."
        r"$$\begin{eqnarray} v^{\phi}_i &=& \frac{Vol(\phi_{s_{i+1}} f - \phi_{s_i} f)}{Vol(f)} \nonumber \\ "
        r"a^{\phi}_i &=& \frac{Area(\phi_{s_{i+1}} f - \phi_{s_i} f)}{Area(f)} \nonumber \\ "
        r"v^{\gamma}_i &=& \frac{Vol(\gamma_{s_i} f - \gamma_{s_{i+1}} f)}{Vol(f)} \nonumber \\ "
        r"a^{\gamma}_i &=& \frac{Area(\gamma_{s_i} f - \gamma_{s_{i+1}} f)}{Area(f)} \end{eqnarray}$$ "
        r"The features $v^{\phi}_i$ and $v^{\gamma}_i$ describe the texture in terms of size of dark and bright "
        r"substructures. If one of these values is particularly high, there were many substructures of this size in the object."
#        r" Note that the last image in the second row of figure\ref{fig:granulometry} looks like an interphase. " 
#        r"We can state, thatthe operators have removed and recorded the difference betweenprometaphase and interphase. " 
        r"There may be a problem with the last structuring element: if the object is too small, the last "
        r"opening will eventually remove the whole object. In this case, we would record an abnormally high value. The " 
        r"features $a^{\gamma}_i$ and $a^{\phi}_i$ describe the irregularity of the shape. Whereas $a^{\phi}_i$ " 
        r"characterize the concavities, $a^{\gamma}_i$ describes prominent spikes. These features are inherently " 
        r"invariant to rotation, translation, and, due to the division by $\mathrm{Vol}(f)$ and $\mathrm{Area}(f)$, to scaling.",
    
    "haralick":
        r"The Haralick features computed on the original gray values. "
        r"Haralick fetaures characterize the texture of objects by means of joint"
        r"distribution of pixel value combinations."
        r"In histograms, one tries to analyze the frequency of certain gray level values in an"
        r"image. The inconvenience of this representation is that the spatial distribution of these"
        r"values is completely lost. One method to address this is to record combinations"
        r"of pixel values at a certain distance. This can be done by the co-occurrence"
        r"matrix depending on distance $d$ and angle $\Phi$, which takes as element $c^{d,\phi}_{i,j}$ "
        r" the number of pixel pairs $x, y$ with distance $d$ at angle $\phi$, fulfilling $f(x) = i$ and $f(y) =j$ "
        r"In order to obtain rotational invariance, the mean of the co-occurrence matrices is calculated for four "
        r"different angles $\phi_i = 0^0, 45^0, 90^0, 145^0$ and for different distances $d =1, 2, 4, 8$. "
        r"Let $$P_{i,j}=\frac{c_{i,j}}{N}$$ be the "
        r"co-occurrence probability for values $i$ and $j$ (for a given distance $d$ in all four angles) and let "
        r"$\mu = \sum_j j \sum_i P(i,j)$ the mean gray level value and $\sigma^2 = \sum_j (j-\mu)^2 \sum_i P(i,j)$ "
        r"its variance. Then, the following features can be calculated from the averaged co-occurrence matrix.<br/><br/>"   
        r"For a detailed discussion on Haralick features, see "
        r"<a class='ref_link' href='#ref-held:05'>[1]</a>",
    
    "haralick-normalized":
        r"The Haralick features computed on the normalized gray values. "
        r"Haralick fetaures characterize the texture of objects by means of joint"
        r"distribution of pixel value combinations."
        r"In histograms, one tries to analyze the frequency of certain gray level values in an"
        r"image. The inconvenience of this representation is that the spatial distribution of these"
        r"values is completely lost. One method to address this is to record combinations"
        r"of pixel values at a certain distance. This can be done by the co-occurrence"
        r"matrix depending on distance $d$ and angle $\Phi$, which takes as element $c^{d,\phi}_{i,j}$ "
        r" the number of pixel pairs $x, y$ with distance $d$ at angle $\phi$, fulfilling $f(x) = i$ and $f(y) =j$ "
        r"In order to obtain rotational invariance, the mean of the co-occurrence matrices is calculated for four "
        r"different angles $\phi_i = 0^0, 45^0, 90^0, 145^0$ and for different distances $d =1, 2, 4, 8$. "
        r"Let $$P_{i,j}=\frac{c_{i,j}}{N}$$ be the "
        r"co-occurrence probability for values $i$ and $j$ (for a given distance $d$ in all four angles) and let "
        r"$\mu = \sum_j j \sum_i P(i,j)$ the mean gray level value and $\sigma^2 = \sum_j (j-\mu)^2 \sum_i P(i,j)$ "
        r"its variance. Then, the following features can be calculated from the averaged co-occurrence matrix.<br/><br/>"   
        r"For a detailed discussion on Haralick features, see "
        r"<a class='ref_link' href='#ref-held:05'>[1]</a>",
    
    "intensity":
        r"Basic intensity features are simple statistics on the original gray value distribution of an object. "
        r"In contrast to texture features basic intensity features cannot describe substructures "
        r"and repeated subpatterns of the object.",
    
    "intensity-normalized":
        r"Basic intensity-normalized features are simple statistics on the <i>normalized</i> gray value distribution of an object. "
        r"In contrast to texture features basic intensity features cannot describe substructures "
        r"and repeated subpatterns of the object.",
    
    "moments":
        r"Moments and derived features have been initially defined to characterize distributions of values (like "
        r"histograms), but they can also be used as shape or texture descriptors. Discrete moments $m_{pq}$ are defined " 
        r" as: $$ \label{equ:moments} m_{pq} = \sum x^p y^q f(x,y)$$ with $f(x,y) \in \{0,1\}$ for shape descriptors "
        r"and $f(x,y)$ the gray level value for gray level descriptors. In pattern recognition tasks where objects are "
        r"to be characterized independently from their position and orientation, translation and rotation invariance are "
        r"required. This can be achieved by several means. One possibility is to use moment invariants <a class ='ref_link' href='#ref-hu:62'>[6]</a> as "
        r"features, i.e. to define polynomial combinations of moments which are invariant with respect to an affine "
        r"transformation. A second possibility is to find the principal axis of the pattern and to calculate the moments "
        r"with respect to this axis and the axis perpendicular to it. This corresponds to a rotation of the object in "
        r"such a way that its principal axis coincides with the x-axis. These moments are called standard moments "
        r"<a class ='ref_link' href='#ref-prokop:92'>[3]</a>."
        "\n"
        r"Furthermore, we can see from equation \ref{equ:moments}, that the moments can be written as $m_{pq} = " 
        r"\langle x^p y^q, f(x,y) \rangle$ with $\langle\cdot, \cdot\rangle$ the scalar product. This means that $m_{pq}$ is nothing else "
        r"than the projection of $f$ on the monomial $x^p y^q$. As the $x^p y^q$ are not orthogonal, the decomposition "
        r"is suboptimal in terms of redundancy. Therefore, the monomials can be replaced by orthogonal polynomials, "
        r"like Zernike or Legendre polynomials. A comparison of the resulting methods can be found in <a class='ref_link' href='#ref-teh:88'>[7]</a>. "
        r"In <a class='ref_link' href='#ref-prokop:92'>[3]</a>, the authors claim that standard moments give similar performance in pattern recognition "
        r"tasks as Zernike moments. We have not followed the approach of Zernike or Legendre moments.",
    
    "statistical-geometry":
        r"Statistical geometric features (or Levelset features) are shape features for different levelsets (i.e. results "
        r"of different thresholds) and, as such, texture features. For each of the following features, a distribution "
        r"of values is calculated according to the set of thresholds. For each of these distributions, the maximal "
        r"feature value, the average feature value, the sample mean and the sample standard deviation are calculated "
        r"as statistics (max_value, avg_value, sample_mean, sample_sd). Furthermore, all features are calculated on "
        r"the foreground and on the background after thresholding.",
    
    }

feature_doc = {
    "convexhull___average-clump-displacement":
      r"difference between the center of gravity of the object and the centers "
      r"of the connected components in $D$, weighted by their area",

    "convexhull___area-ratio":
      r"ratio of the area of the "
      r"object to the area of its convex hull. This feature equals 1 for "
      r"convex sets, if not, it is smaller",

    "convexhull___number-of-connected-components":
      r"number of connected components of $D$",

    "convexhull___area-max-0":
      r"area of the biggest connected components of $D$.",

    "convexhull___area-max-1":
      r"area of the second biggest connected components of $D$.",

    "convexhull___area-max-2":
      r"area of the thrid biggest connected components of $D$.",

    "convexhull___area-mean":
      r"mean area of the connected components of $D$.",

    "convexhull___rugosity":
      r"ratio of the perimeter of the "
      r"object to the perimeter of its convex hull. "
      r"For convex objects, this feature equals 1, if "
      r"the object is not convex, it is smaller than 1",

    "convexhull___number-of-large-connected-components":
      r"number of large connected components (larger than a certain threshold) of $D$",

    "convexhull___area-variance":
      r"area variance of the connected components of $D$",

    "circularity___standard":
      r"rough estimation of the 'roundness' of the object: "
      r"$$\frac{P}{2 \sqrt{\pi N}}$$"
      r"It should be one for a perfect circle, becoming larger with decreasing similarity to a circle",

    "expansion___max":
      r"maximal distance $\Delta_{\max}$ between center of gravity and border pixels",

    "expansion___min":
      "minimal distance $\Delta_{\min}$ between center of gravity and border pixels",

    "expansion___ratio":
      r"ratio of minimal to maximal distance between center of gravity and border pixels (which takes 1 as a"
      "maximal value for a perfectly round object and 0 for an object with the center of gravity lying on its "
      "border (due to a strong concavity)",

    "distance-map-dynamics___number-of-maxima":
      r"number of maxima in the distance map",

    "distance-map-dynamics___radius":
      r"radius of the first four highest dynamics of the distance map",

    "eccentricity___":
      "like circularity, but under the hypothesis of an ellipse",

    "ellipse___ratio-axis":
      r"ratio of minor axis to major axis",

    "ellipse___major-axis":
      r"length of major axis of the ellipse having the same second order moments as the object",

    "ellipse___minor-axis":
      r"length of minor axis of the ellipse having the same second order moments as the object",

    "granulometry___area-1":
      r"Normalized change of area after applying subsequent moprhological operations $\Omega_{s_i}$ with $s_i = 1$: "
      r"$$\frac{\mathrm{Area}(\Omega_1 f - \Omega_0 f)}{\mathrm{Area}(f)}$$",

    "granulometry___area-2":
     r"Normalized change of area after applying subsequent moprhological operations $\Omega_{s_i}$ with $s_i = 2$: "
      r"$$\frac{\mathrm{Area}(\Omega_2 f - \Omega_1 f)}{\mathrm{Area}(f)}$$",

    "granulometry___area-3":
      r"Normalized change of area after applying subsequent moprhological operations $\Omega_{s_i}$ with $s_i = 3$: "
      r"$$\frac{\mathrm{Area}(\Omega_3 f - \Omega_2 f)}{\mathrm{Area}(f)}$$",

    "granulometry___area-5":
      r"Normalized change of area after applying subsequent moprhological operations $\Omega_{s_i}$ with $s_i = 5$: "
      r"$$\frac{\mathrm{Area}(\Omega_5 f - \Omega_3 f)}{\mathrm{Area}(f)}$$",

    "granulometry___area-7":
      r"Normalized change of area after applying subsequent moprhological operations $\Omega_{s_i}$ with $s_i = 7$: "
      r"$$\frac{\mathrm{Area}(\Omega_7 f - \Omega_5 f)}{\mathrm{Area}(f)}$$",

    "granulometry___volume-1":
      r"Normalized change of volume after applying subsequent moprhological operations $\Omega_{s_i}$ with $s_i = 1$: "
      r"$$\frac{\mathrm{Vol}(\Omega_1 f - \Omega_0 f)}{\mathrm{Vol}(f)}$$",

    "granulometry___volume-2":
      r"Normalized change of volume after applying subsequent moprhological operations $\Omega_{s_i}$ with $s_i = 2$: "
      r"$$\frac{\mathrm{Vol}(\Omega_2 f - \Omega_1 f)}{\mathrm{Vol}(f)}$$",

    "granulometry___volume-3":
      r"Normalized change of volume after applying subsequent moprhological operations $\Omega_{s_i}$ with $s_i = 3$: "
      r"$$\frac{\mathrm{Vol}(\Omega_3 f - \Omega_2 f)}{\mathrm{Vol}(f)}$$",

    "granulometry___volume-5":
      r"Normalized change of volume after applying subsequent moprhological operations $\Omega_{s_i}$ with $s_i = 5$: "
      r"$$\frac{\mathrm{Vol}(\Omega_5 f - \Omega_3 f)}{\mathrm{Vol}(f)}$$",

    "granulometry___volume-7":
      r"Normalized change of volume after applying subsequent moprhological operations $\Omega_{s_i}$ with $s_i = 7$: "
      r"$$\frac{\mathrm{Vol}(\Omega_7 f - \Omega_5 f)}{\mathrm{Vol}(f)}$$",

    "gyration___radius":
      r"radius of a circle centered in the origin with the same second order moments as the object",

    "gyration___ratio":
      r"ratio of the gyration radius to the maximal distance $\Delta_{max}$",

    "haralick___ASM":
      r"Angular Second Moment (Energy) $$\sum P_{i,j}^2$$",

    "haralick___CON":
      r"Contrast (Inertia) $$\sum P_{i,j}(i-j)^2$$",

    "haralick___COR":
      r"Correlation $$- \sum \frac{(i-\mu)(j-\mu)}{\sigma^2} P(i,j)$$",

    "haralick___COV":
      r"Coefficient of variation $$\frac{\sigma^2}{\mu}$$",

    "haralick___DAV":
      r"Difference average $$\sum_k k \sum_{|i-j|=k} P(i,j)$$",

    "haralick___ENT":
      r"Entropy $$- \sum P_{i,j} \log{P_{i,j}}$$",

    "haralick___IDM":
      r"Inverse Difference Moment (Homogeneity) $$\sum \frac{P_{i,j}}{1 + (i-j)^2}$$",

    "haralick___PRO":
      r"Prominence $$\sum (i+j-2\mu)^4 P(i,j)$$",

    "haralick___SAV":
      r"Sum average: the average of partial sums, subject to the condition $|i+j| = k$: "
      r"$$\sum_k k \sum_{|i+j|=k} P(i,j)$$",

    "haralick___SET":
      r"Sum entropy $$\sum_k \sum_{|i-j|=k} P(i,j) \log{\sum_{|i-j|=k} P(i,j)}$$",

    "haralick___SHA":
      r"Shade $$\sum (i+j-2\mu)^3 P(i,j)$$",

    "haralick___SVA":
      r"Sum variance $$\sum_k (k - SAV)^2 \sum_{|i-j|=k} P(i,j)$$",

    "haralick___VAR":
      r"Variance $$\sum (i-\mu)^2 P(i,j)$$",

    "haralick___average":
      r"Average $\mu$",

    "haralick___variance ":
      r"Variance $\sigma^2$",

    "haralick-normalized___ASM":
      r"Angular Second Moment (Energy) $$\sum P_{i,j}^2$$",

    "haralick-normalized___CON":
      r"Contrast (Inertia) $$\sum P_{i,j}(i-j)^2$$",

    "haralick-normalized___COR":
      r"Correlation $$- \sum \frac{(i-\mu)(j-\mu)}{\sigma^2} P(i,j)$$",

    "haralick-normalized___COV":
      r"Coefficient of variation $$\frac{\sigma^2}{\mu}$$",

    "haralick-normalized___DAV":
      r"Difference average $$\sum_k k \sum_{|i-j|=k} P(i,j)$$",

    "haralick-normalized___ENT":
      r"Entropy $$- \sum P_{i,j} \log{P_{i,j}}$$",

    "haralick-normalized___IDM":
      r"Inverse Difference Moment (Homogeneity) $$\sum \frac{P_{i,j}}{1 + (i-j)^2}$$",

    "haralick-normalized___PRO":
      r"Prominence $$\sum (i+j-2\mu)^4 P(i,j)$$",

    "haralick-normalized___SAV":
      r"Sum average: the average of partial sums, subject to the condition $|i+j| = k$: "
      r"$$\sum_k k \sum_{|i+j|=k} P(i,j)$$",

    "haralick-normalized___SET":
      r"Sum entropy $$\sum_k \sum_{|i-j|=k} P(i,j) \log{\sum_{|i-j|=k} P(i,j)}$$",

    "haralick-normalized___SHA":
      r"Shade $$\sum (i+j-2\mu)^3 P(i,j)$$",

    "haralick-normalized___SVA":
      r"Sum variance $$\sum_k (k - SAV)^2 \sum_{|i-j|=k} P(i,j)$$",

    "haralick-normalized___VAR":
      r"Variance $$\sum (i-\mu)^2 P(i,j)$$",

    "haralick-normalized___average":
      r"Average $\mu$",

    "haralick-normalized___variance ":
      r"Variance $\sigma^2$",

    "circularity___robust-avg":
      r"robust way of calculating circularity, as it does not rely on the perimeter, but on the maximal "
      r"distance $\Delta_{max}$: "
      r"$$\frac{1 + \sqrt{\pi}\Delta_{max} }{\sqrt{N}} - 1$$ " 
      r"The measure tends towards 0 for a perfect circle",

    "circularity___robust-max":
      r"robust way of calculating circularity, as it does not rely on the perimeter, but on the average "
      r"distance  $\overline{\Delta}$: "
      r"$$\frac{1 + \sqrt{\pi}\overline{\Delta} }{\sqrt{N}} - 1$$ " 
      r"The measure tends towards 0 for a perfect circle",

    "statistical-geometry___CAREA_avgerage":
      r"Average average-clump-area (average area of the connected components)",

    "statistical-geometry___CAREA_max":
      r"Maximal average-clump-area (average area of the connected components)",

    "statistical-geometry___CAREA_sample_average":
      r"Sample average average-clump-area (average area of the connected components)",

    "statistical-geometry___CAREA_sample_standard-deviation":
      r"Sample standard deviation of average-clump-area (average area of the connected components)",

    "statistical-geometry___DISP_avgerage":
      r"Average average-clump-displacement "
      r"(estimation of the average distance between center of gravity of the "
      r"connected component and the center of gravity of the object)",

    "statistical-geometry___DISP_max":
      r"Maximal average-clump-displacement "
      r"(estimation of the average distance between center of gravity of the "
      r"connected component and the center of gravity of the object)",

    "statistical-geometry___DISP_sample_average":
      r"Sample average average-clump-displacement "
      r"(estimation of the average distance between center of gravity of the "
      r"connected component and the center of gravity of the object)",

    "statistical-geometry___DISP_sample_standard-deviation":
      r"Sample standard deviation of average-clump-displacement "
      r"(estimation of the average distance between center of gravity of the "
      r"connected component and the center of gravity of the object)",

    "statistical-geometry___INTERIA_avgerage":
      r"Average average-clump-interia (like "
      r"average clump displacement, but weighted by the area of each "
      r"connected component)",

    "statistical-geometry___INTERIA_max":
      r"Maximal average-clump-interia (like "
      r"average clump displacement, but weighted by the area of each "
      r"connected component)",

    "statistical-geometry___INTERIA_sample_average":
      r"Sample average average-clump-interia (like "
      r"average clump displacement, but weighted by the area of each "
      r"connected component)",

    "statistical-geometry___INTERIA_sample_standard-deviation":
      r"Sample standard deviation average-clump-interia (like "
      r"average clump displacement, but weighted by the area of each "
      r"connected component)",

    "statistical-geometry___IRGL_avgerage":
      r"Average irregularity",

    "statistical-geometry___IRGL_max":
      r"Maximal irregularity",

    "statistical-geometry___IRGL_sample_average":
      r"Sample average irregularity",

    "statistical-geometry___IRGL_sample_standard-deviation":
      r"Sample standard deviation of irregularity",

    "statistical-geometry___NCA_avgerage":
      r"Average normalized number of connected "
      r"components (number of connected components divided by the area of the "
      r"object)",

    "statistical-geometry___NCA_max":
      r"Maximal normalized number of connected "
      r"components (number of connected components divided by the area of the "
      r"object)",

    "statistical-geometry___NCA_sample_average":
      r"Sample average normalized number of connected "
      r"components (number of connected components divided by the area of the "
      r"object)",

    "statistical-geometry___NCA_sample_standard-deviation":
      r"Sample standard deviation of normalized number of connected "
      r"components (number of connected components divided by the area of the "
      r"object)",

    "statistical-geometry___TAREA_avgerage":
      r"Average total clump area",

    "statistical-geometry___TAREA_max":
      r"Maximal total clump area",

    "statistical-geometry___TAREA_sample_average":
      r"Sample average total clump area",

    "statistical-geometry___TAREA_sample_standard-deviation":
      r"Sample standard deviation of total clump area",

    "algebraic-invariant___":
      r"The $I$th Hu-moment (algebraic invarient)",

    "intensity___avgerage":
      r"average original gray value",

    "intensity___standard-deviation":
      r"standard deviation of the original gray values",

    "intensity___weighted-avgerage":
      r"average original gray values weighted by the distance between the pixel and center of gravity: "
      r"$$\frac{1}{N}\sum |x - \overline{x}| f(x)$$",

    "intensity___weighted-distance":
      r"average distance to the center of gravity: "
      r"$$\frac{1}{N}\sum |x - \overline{x}|$$",

    "intensity___weighted-inverse-avgerage":
      r"average original gray values weighted by the inverse distance between the pixel and center of gravity: "
      r"$$\frac{1}{N}\sum\frac{f(x)}{|x - \overline{x}| + 1}$$",

    "intensity-normalized___avgerage":
      r"average normalized gray value",

    "intensity-normalized___standard-deviation":
      r"standard deviation of the normalized gray values",

    "intensity-normalized___weighted-avgerage":
      r"average normalized gray values weighted by the distance between the pixel and center of gravity: "
      r"$$\frac{1}{N}\sum |x - \overline{x}| f(x)$$",

    "intensity-normalized___weighted-distance":
      r"average distance to the center of gravity: "
      r"$$\frac{1}{N}\sum |x - \overline{x}|$$",

    "intensity-normalized___weighted-inverse-avgerage":
      r"average normalized gray values weighted by the inverse distance between the pixel and center of gravity: "
      r"$$\frac{1}{N}\sum\frac{f(x)}{|x - \overline{x}| + 1}$$",

    "perimeter___":
      r"object perimeter $P$",

    "principle_gyration___ratio":
      r"ratio of the two principle_gyrations",

    "principle_gyration___x":
      r"distance between the principal axis and a line with the same second order moment as the object",

    "principle_gyration___y":
      r"distance between the axis perpendicular "
      r"to the principal one and a line with the same second order moment as "
      r"the object",

    "area___":
      r"number of object pixels $N$",

    "skewness___x":
      r"projection skewness (normalized third order "
      r"moment) in the direction of the principal axis",

    "skewness___y":
      r"projection skewness (normalized third order "
      r"moment) in the direction perpendicular to the principal axis",
}

github_prefix = "https://github.com/CellCognition/cecog/blob/master/"
feature_githublink = {
    "convexhull___average-clump-displacement": ("csrc/include/cecog/containers.hxx", 990,990),
    "convexhull___area-ratio": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___number-of-connected-components": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___area-max-0": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___area-max-1": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___area-max-2": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___area-mean": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___rugosity": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___number-of-large-connected-components": ("csrc/include/cecog/features.hxx", 990,990),
    "convexhull___area-variance": ("csrc/include/cecog/features.hxx", 990,990),
    "circularity___standard": ("csrc/include/cecog/features.hxx", 990,990),
    "expansion___max": ("csrc/include/cecog/features.hxx", 990,990),
    "expansion___min": ("csrc/include/cecog/features.hxx", 990,990),
    "expansion___ratio": ("csrc/include/cecog/features.hxx", 990,990),
    "distance-map-dynamics___number-of-maxima": ("csrc/include/cecog/features.hxx", 990,990),
    "distance-map-dynamics___radius": ("csrc/include/cecog/features.hxx", 990,990),
    "eccentricity___": ("csrc/include/cecog/features.hxx", 990,990),
    "ellipse___ratio-axis": ("csrc/include/cecog/features.hxx", 990,990),
    "ellipse___major-axis": ("csrc/include/cecog/features.hxx", 990,990),
    "ellipse___minor-axis": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___area-1": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___area-2": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___area-3": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___area-5": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___area-7": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___volume-1": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___volume-2": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___volume-3": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___volume-5": ("csrc/include/cecog/features.hxx", 990,990),
    "granulometry___volume-7": ("csrc/include/cecog/features.hxx", 990,990),
    "gyration___radius": ("csrc/include/cecog/features.hxx", 990,990),
    "gyration___ratio": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___ASM": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___CON": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___COR": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___COV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___DAV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___ENT": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___IDM": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___PRO": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___SAV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___SET": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___SHA": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___SVA": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___VAR": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___average": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick___variance ": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___ASM": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___CON": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___COR": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___COV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___DAV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___ENT": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___IDM": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___PRO": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___SAV": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___SET": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___SHA": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___SVA": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___VAR": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___average": ("csrc/include/cecog/features.hxx", 990,990),
    "haralick-normalized___variance ": ("csrc/include/cecog/features.hxx", 990,990),
    "circularity___robust-avg": ("csrc/include/cecog/features.hxx", 990,990),
    "circularity___robust-max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___CAREA_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___CAREA_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___CAREA_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___CAREA_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___DISP_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___DISP_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___DISP_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___DISP_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___INTERIA_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___INTERIA_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___INTERIA_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___INTERIA_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___IRGL_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___IRGL_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___IRGL_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___IRGL_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___NCA_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___NCA_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___NCA_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___NCA_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___TAREA_avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___TAREA_max": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___TAREA_sample_average": ("csrc/include/cecog/features.hxx", 990,990),
    "statistical-geometry___TAREA_sample_standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "algebraic-invariant___": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity___avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity___standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity___weighted-avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity___weighted-distance": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity___weighted-inverse-avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity-normalized___avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity-normalized___standard-deviation": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity-normalized___weighted-avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity-normalized___weighted-distance": ("csrc/include/cecog/features.hxx", 990,990),
    "intensity-normalized___weighted-inverse-avgerage": ("csrc/include/cecog/features.hxx", 990,990),
    "perimeter___": ("csrc/include/cecog/features.hxx", 990,990),
    "principle_gyration___ratio": ("csrc/include/cecog/features.hxx", 990,990),
    "principle_gyration___x": ("csrc/include/cecog/features.hxx", 990,990),
    "principle_gyration___y": ("csrc/include/cecog/features.hxx", 990,990),
    "area___": ("csrc/include/cecog/features.hxx", 990,990),
    "skewness___x": ("csrc/include/cecog/features.hxx", 990,990),
    "skewness___y": ("csrc/include/cecog/features.hxx", 990,990),
}

parameter_doc = {
    "I" : "",
    "on": "",
    "distance": "",
    "angular-step": "",
    "operation": "",
    "highest": "",
                 }

reference_doc = {
    1:'neumann:06', 
    2:'held:05', 
    3:'prokop:92', 
    4:'serra:83', 
    5:'angulo_thesis:03',
    6:'hu:62', 
    7:'teh:88',
    8:'grimaud_thesis:91'}